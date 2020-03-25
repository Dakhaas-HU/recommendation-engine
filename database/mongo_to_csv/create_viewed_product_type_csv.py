from recommendation_engine.database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/viewed_product_type.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'product_type_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_product_type.csv')

    for item in data:
        product_types = item['preferences']['product_type']
        for product_type in product_types:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': product_type['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'product_type_name': product_type})
            except KeyError:
                lineDic.update({'product_type_name': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_product_type.csv')