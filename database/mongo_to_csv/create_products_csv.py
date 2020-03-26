import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/products.csv", "w+", encoding="utf-8")

data = database.products.find()

with file:
    fnames = ['product_id', 'brand', 'category', 'color', 'description', 'gender', 'name', 'selling_price',
              'recommandable', 'sub_category', 'sub_sub_category', 'availability',
              'discount', 'target_group', 'unit', 'online_only', 'series', 'sort', 'type', 'variant', 'fragance_type',
              'type_hair_care', 'type_hair_color'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating product.csv')

    for item in data:
        lineDic = {}
        try:
            lineDic.update({'product_id': item['_id']})
        except KeyError:
            lineDic.update({'product_id': None})

        try:
            lineDic.update({'brand': item['brand']})
        except KeyError:
            lineDic.update({'brand': None})

        try:
            lineDic.update({'category': item['category']})
        except KeyError:
            lineDic.update({'category': None})

        try:
            lineDic.update({'color': item['color']})
        except KeyError:
            lineDic.update({'color': None})

        try:
            lineDic.update({'description': item['description']})
        except KeyError:
            lineDic.update({'description': None})

        try:
            lineDic.update({'gender': item['gender']})
        except KeyError:
            lineDic.update({'gender': None})

        try:
            lineDic.update({'name': item['name']})
        except KeyError:
            lineDic.update({'name': None})

        try:
            lineDic.update({'selling_price': item['price']['mrsp']})
        except KeyError:
            lineDic.update({'selling_price': None})

        try:
            lineDic.update({'recommandable': item['price']['recommendable']})
        except KeyError:
            lineDic.update({'recommandable': None})

        try:
            lineDic.update({'sub_category': item['sub_category']})
        except KeyError:
            lineDic.update({'sub_category': None})

        try:
            lineDic.update({'sub_sub_category': item['sub_sub_category']})
        except KeyError:
            lineDic.update({'sub_sub_category': None})

        try:
            lineDic.update({'availability': item['properties']['availability']})
        except KeyError:
            lineDic.update({'availability': None})

        try:
            lineDic.update({'discount': item['properties']['discount']})
        except KeyError:
            lineDic.update({'discount': None})

        try:
            lineDic.update({'target_group': item['properties']['doelgroep']})
        except KeyError:
            lineDic.update({'target_group': None})

        try:
            lineDic.update({'unit': item['properties']['eenheid']})
        except KeyError:
            lineDic.update({'unit': None})

        try:
            lineDic.update({'online_only': item['properties']['online_only']})
        except KeyError:
            lineDic.update({'online_only': None})

        try:
            lineDic.update({'series': item['properties']['serie']})
        except KeyError:
            lineDic.update({'series': None})

        try:
            lineDic.update({'sort': item['properties']['sort']})
        except KeyError:
            lineDic.update({'sort': None})

        try:
            lineDic.update({'type': item['properties']['type']})
        except KeyError:
            lineDic.update({'type': None})

        try:
            lineDic.update({'variant': item['properties']['variant']})
        except KeyError:
            lineDic.update({'variant': None})

        try:
            lineDic.update({'fragance_type': item['properties']['geursoort']})
        except KeyError:
            lineDic.update({'fragance_type': None})

        try:
            lineDic.update({'type_hair_care': item['properties']['soorthaarverzorging']})
        except KeyError:
            lineDic.update({'type_hair_care': None})

        try:
            lineDic.update({'type_hair_color': item['properties']['typehaarkleuring']})
        except KeyError:
            lineDic.update({'type_hair_color': None})

        writer.writerow(lineDic)
file.close()
print('Finished creating product.csv')