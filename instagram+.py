# Python program to read
# json file


import json

# Opening JSON file
f = open('yessirskiiiiCO.json', encoding="utf8")
print(f)
# returns JSON object as
# a dictionary
data = json.load(f)
#print(data)

# Iterating through the json
# list

comments = []
for x in range(len(data["GraphImages"])):
    comments.append(data["GraphImages"][x]["edge_media_to_comment"]["data"])

comments2 = []


# ["edge_media_to_comment"].values
print(comments)

# Closing file
f.close()




