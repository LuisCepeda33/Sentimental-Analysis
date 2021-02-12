import json
import re

# Opening JSON file
f = open('samuelgarcias.json', encoding="utf8")
data = json.load(f)

#print(type(data))


def cleantxt(text):
    text = re.sub(r'@[A-Za-z0-9:_]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text


def extract_comments_users(dats):
    info = []
    for x in range(len(dats["GraphImages"])):
        info.append(dats["GraphImages"][x]["comments"]["data"])

    picWcomment = []
    for i in range(len(info)):
        if len(info[i]) == 0:
            pass
        else:
            picWcomment.append(info[i])

    a = picWcomment[0]

    comments = []
    for z in range(len(picWcomment)):
        for x in range(len(picWcomment[z])):
            comments.append(picWcomment[z][x]["text"])

    a = comments
    txtclean = []
    for i in range(len(a)):
        txtclean.append(cleantxt(a[i]))
    return txtclean






