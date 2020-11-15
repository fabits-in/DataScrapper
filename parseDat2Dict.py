name = f"raw/name"
f = open(name, 'r')
lines = f.read().split("\n")
dict={}
# for i in range(len(lines)):
#     if i==0:
#         continue
#     else:
#         elem = lines[i].split(",")
#         for x in  range(len(elem)):
#             if x==1:
#                 dict[elem[x]]=int(elem[x+2])

for i in range(len(lines)):
    elem = lines[i].split(",")
    if elem[0]=="Record Type":
        for x in range(i+1,len(lines)-1):
            ele = lines[x].split(",")
            for y in  range(len(ele)):
                if y==2:
                    dict[ele[y]]=int(ele[y+3])
        break

print(dict)