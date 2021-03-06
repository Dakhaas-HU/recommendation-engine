import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB().huwebshop
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/viewed_brand.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'brand_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter='#')
    print('Started creating viewed_brand.csv')

    for item in data:
        try:
            brands = item['preferences']['brand']
            for brand in brands:
                lineDic = {}
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': brands[brand]['views']})
                except KeyError:
                    lineDic.update({'views': None})

                try:
                    lineDic.update({'brand_name': brand})
                except KeyError:
                    lineDic.update({'brand_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_brand.csv')