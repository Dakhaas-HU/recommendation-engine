import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/viewed_product_size.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'product_size_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_product_size.csv')

    for item in data:
        try:
            product_sizes = item['preferences']['product_size']
            for product_size in product_sizes:
                lineDic = {}
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': product_sizes[product_size]['views']})
                except KeyError:
                    lineDic.update({'views': None})


                try:
                    lineDic.update({'product_size_name': product_size})
                except KeyError:
                    lineDic.update({'product_size_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_product_size.csv')