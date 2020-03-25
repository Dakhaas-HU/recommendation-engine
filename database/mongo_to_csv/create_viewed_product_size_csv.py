from recommendation_engine.database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/viewed_product_size.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'product_size_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_product_size.csv')

    for item in data:
        product_sizes = item['preferences']['product_size']
        for product_size in product_sizes:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': product_size['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'product_size_name': product_size})
            except KeyError:
                lineDic.update({'product_size_name': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_product_size.csv')