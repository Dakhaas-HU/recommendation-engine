import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/viewed_product_type.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'product_type_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames, quoting='#')
    print('Started creating viewed_product_type.csv')

    for item in data:
        try:
            product_types = item['preferences']['product_type']
            for product_type in product_types:
                lineDic = {}
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': product_type['views']})
                except KeyError:
                    lineDic.update({'views': None})
                except TypeError:
                    lineDic.update({'views': None})

                try:
                    lineDic.update({'product_type_name': product_type})
                except KeyError:
                    lineDic.update({'product_type_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_product_type.csv')