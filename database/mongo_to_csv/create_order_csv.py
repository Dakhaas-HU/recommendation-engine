from database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/order.csv", "w+", encoding="utf-8")

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
