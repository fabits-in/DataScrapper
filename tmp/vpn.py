#!/usr/bin/env python
"""
Copyright 2011 Domen Kozar. All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:
   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.
   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.
THIS SOFTWARE IS PROVIDED BY DOMEN KOZAR ''AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DOMEN KOZAR OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of DOMEN KOZAR.
USAGE
=====
1) clone gist somewhere (eg. /home/user/autovpn/)
2) add to /etc/rc.local: python /home/user/autovpn/autovpn.py "myvpn" 'Auto homenetwork,Auto worknetwork' >> /var/log/autovpn.log&
3) reboot :-)
CHANGELOG
=========
0.2 (28.01.2012)
----------------
* feature: use logging module
* bug: script would fail if there was no active connection
0.1 (01.01.2012)
----------------
* bug: compatible with NM 0.9, dropped support for 0.8
* feature: specify networks that vpn is not autoconnected
KNOWN ISSUES
============
* it will always use first active network connection
"""
import sys
import logging

from dbus.mainloop.glib import DBusGMainLoop
import dbus
import gobject

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename='/var/log/autovpn.log',
    filemode='a',
)


class AutoVPN(object):
    """Solves two jobs, tested with NetworkManager 0.9.x:
    * if VPN connection is not disconnected by user himself, reconnect (configurable max_attempts)
    * on new active network connection, activate VPN
    :param vpn_name: Name of VPN connection that will be used for autovpn
    :param ignore_networks: Comma separated network names in NM that will not force VPN usage
    :param max_attempts: Maximum number of attempts of reconnection VPN session on failures
    :param delay: Miliseconds to wait before reconnecting VPN
    """

    def __init__(self, vpn_name, ignore_networks='', max_attempts=5, delay=5000):
        self.vpn_name = vpn_name
        self.max_attempts = max_attempts
        self.delay = delay
        self.failed_attempts = 0
        self.bus = dbus.SystemBus()
        self.ignore_networks = filter(None, ignore_networks.split(','))
        self.get_network_manager().connect_to_signal("StateChanged", self.onNetworkStateChanged)
        logger.info("Maintaining connection for %s, reattempting up to %d times with %d ms between retries", vpn_name,
                    max_attempts, delay)

    def onNetworkStateChanged(self, state):
        """Handles network status changes and activates the VPN on established connection."""
        logger.debug("Network state changed: %d", state)
        if state == 70:
            self.activate_vpn()

    def onVpnStateChanged(self, state, reason):
        """Handles different VPN status changes and eventually reconnects the VPN."""
        # vpn connected or user disconnected manually?
        if state == 5 or (state == 7 and reason == 2):
            self.failed_attempts = 0
            if state == 5:
                logger.info("VPN %s connected", self.vpn_name)
            else:
                logger.info("User disconnected manually")
            return
        # connection failed or unknown?
        elif state in [6, 7]:
            # reconnect if we haven't reached max_attempts
            if not self.max_attempts or self.failed_attempts < self.max_attempts:
                logger.info("Connection failed, attempting to reconnect")
                self.failed_attempts += 1
                gobject.timeout_add(self.delay, self.activate_vpn)
            else:
                logger.info("Connection failed, exceeded %d max attempts.", self.max_attempts)
                self.failed_attempts = 0

    def get_network_manager(self):
        """Gets the network manager dbus interface."""
        logger.debug("Getting NetworkManager DBUS interface")
        proxy = self.bus.get_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager')
        return dbus.Interface(proxy, 'org.freedesktop.NetworkManager')

    def get_vpn_interface(self, name):
        'Gets the VPN connection interface with the specified name.'
        logger.debug("Getting %s VPN connection DBUS interface", name)
        proxy = self.bus.get_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager/Settings')
        iface = dbus.Interface(proxy, 'org.freedesktop.NetworkManager.Settings')
        connections = iface.ListConnections()
        for connection in connections:
            proxy = self.bus.get_object('org.freedesktop.NetworkManager', connection)
            iface = dbus.Interface(proxy, 'org.freedesktop.NetworkManager.Settings.Connection')
            con_settings = iface.GetSettings()['connection']
            if con_settings['type'] == 'vpn' and con_settings['id'] == name:
                logger.debug("Got %s interface", name)
                return iface
        logger.error("Unable to acquire %s VPN interface. Does it exist?", name)
        return None

    def get_active_connection(self):
        """Gets the dbus interface of the first active
        network connection or returns None.
        """
        logger.debug("Getting active network connection")
        proxy = self.bus.get_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager')
        iface = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties')
        active_connections = iface.Get('org.freedesktop.NetworkManager', 'ActiveConnections')
        if len(active_connections) == 0:
            logger.info("No active connections found")
            return None
        logger.info("Found %d active connection(s)", len(active_connections))
        return active_connections[0]

    def activate_vpn(self):
        """Activates the vpn connection."""
        logger.info("Activating %s VPN connection", self.vpn_name)
        vpn_con = self.get_vpn_interface(self.vpn_name)
        active_con = self.get_active_connection()
        if active_con is None:
            return

        # check if we have to ignore vpn
        proxy = self.bus.get_object('org.freedesktop.NetworkManager', active_con)
        con = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties').Get(
            'org.freedesktop.NetworkManager.Connection.Active', 'Connection')
        proxy = self.bus.get_object('org.freedesktop.NetworkManager', con)
        settings = dbus.Interface(proxy, 'org.freedesktop.NetworkManager.Settings.Connection').GetSettings()
        if settings['connection']['id'] in self.ignore_networks:
            logger.info("Ignored network connection %s based on settings", settings['connection']['id'])
            return

        # activate vpn and watch for reconnects
        if vpn_con and active_con:
            new_con = self.get_network_manager().ActivateConnection(
                vpn_con,
                dbus.ObjectPath("/"),
                active_con,
            )
            proxy = self.bus.get_object('org.freedesktop.NetworkManager', new_con)
            iface = dbus.Interface(proxy, 'org.freedesktop.NetworkManager.VPN.Connection')
            iface.connect_to_signal('VpnStateChanged', self.onVpnStateChanged)
            logger.info("VPN %s should be active (soon)", self.vpn_name)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: autovpn VPN_CONNECTION_NAME <COMMA SEPARATED NAMES OF IGNORABLE NETWORKS>')
        print('-> activates vpn if any network connection is active')
        print('-> and reconnects VPN on failure')
        sys.exit(0)

    # set up the main loop
    DBusGMainLoop(set_as_default=True)
    loop = gobject.MainLoop()
    # TODO: argparse
    if len(sys.argv) > 2:
        AutoVPN(sys.argv[1], sys.argv[2])
    else:
        AutoVPN(sys.argv[1])
    loop.run()
