from recommendation_engine.database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/previously_recommended.csv", "w+")

data = database.profiles.find()

with file:
    fnames = ['profile_id', 'product_id'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating previously_recommended.csv')

    for item in data:
        product_ids = item['previously_recommended']
        for id in product_ids:
            lineDic = {}
            print(id)
            try:
                lineDic.update({'profile_id': item['_id']})
            except KeyError:
                lineDic.update({'profile_id': None})

            try:
                lineDic.update({'product_id': id})
            except KeyError:
                lineDic.update({'product_id': None})


            writer.writerow(lineDic)
file.close()
print('Finished creating previously_recommended.csv')