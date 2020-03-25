from recommendation_engine.database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/viewed_brand.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'brand_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_brand.csv')

    for item in data:
        brands = item['preferences']['brand']
        for brand in brands:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': brand['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'brand_name': brand})
            except KeyError:
                lineDic.update({'brand_name': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_brand.csv')