import json

with open('test.json') as json_file:
    data = json.load(json_file)
    json_file.close()

for user in data:
    print(data[user])
