import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/order.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'product_id'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating order.csv')
    for item in data:
        lineDic = {}
        try:
            products = item['order']['products']
            for id in products:
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'product_id': id['id']})
                except KeyError and TypeError:
                    lineDic.update({'product_id': None})
                writer.writerow(lineDic)
        except KeyError:
            continue
        except TypeError:
            continue
file.close()
print('Finished creating order.csv')
