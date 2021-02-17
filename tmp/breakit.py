f = open("raw")
i = 1
c = 0
f1 = open(f"s{i}", 'w')
chunk = 2500
line = f.readline()
while line != '':
    f1.write(line)
    c += 1
    if c == chunk:
        c = 0
        i += 1
        f1.close()
        f1 = open(f"s{i}", 'w')
    line = f.readline()
f.close()
f1.close()
