import json

# Opening JSON file
f = open('honeybadgerlatte.json', encoding="utf8")
data = json.load(f)


def extract_comments_tags(dat):
    dic = []
    for x in range(len(dat["GraphImages"])):
        dic.append(data["GraphImages"][x]["edge_media_to_comment"]["data"])

    no_empty = []
    for y in range(len(dic)):
        if len(dic[y]) == 0:
            pass
        else:
            no_empty.append(dic[y])

    comments = []
    for z in range(len(no_empty)):
        for x in range(len(no_empty[z])):
            comments.append(no_empty[z][x]["text"])

    return comments

f.close()



print(extract_comments_tags(data))





