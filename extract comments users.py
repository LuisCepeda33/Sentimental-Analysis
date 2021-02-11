import json

# Opening JSON file
f = open('furro33.json', encoding="utf8")
data = json.load(f)

print(type(data))

#####NA
info = []
for x in range(len(data["GraphImages"])):
    info.append(data["GraphImages"][x]["comments"])

print(info[0]["data"])
data = []
for y in range(len(info[0]["data"])):
    data.append(info[0]["data"][0])

print(data[0])



#for z in range(len(info)):
#    print(info[z])

#print(info[0])
#for t in range(len(info[0]))



no_empty = []
for y in range(len(info)):
    if len(info[y]) == 0:
        pass
    else:
        no_empty.append(info[y])




