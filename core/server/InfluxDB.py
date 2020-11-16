from influxdb_client import InfluxDBClient, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDB:

    def __init__(self):
        token = "BAz_tvCiF48nA94hRgb9JD16Kh0GwuHOhjUuZtaKxGd8Ue03UeXZMbLFPv1arM3MzxpPpU_DVgcwrW1oOYrKvg=="
        self.org = "fabits"
        server = "localhost"
        port = "8086"
        self.client = InfluxDBClient(url=f"http://{server}:{port}", token=token)

    def write_data(self, data):
        bucket = "historical_data"
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket, self.org, data, write_precision=WritePrecision.S)
