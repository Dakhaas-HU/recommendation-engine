""""
filling_products.py
====================================
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]
mycol = mydb["products"]


counter = []
for item in mycol.find():
    if 'name' in item:
        if item['name'] is not None:
            name = item['name'].split(' ')
            if name[0] not in counter:
                counter.append(name[0])

print(counter)
