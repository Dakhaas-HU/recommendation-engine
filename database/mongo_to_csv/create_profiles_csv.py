from recommendation_engine.database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/profiles.csv", "w+")

data = database.profiles.find()

with file:
    fnames = ['profile_id', 'segment'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating profiles.csv')

    for item in data:
        lineDic = {}
        print(item)
        try:
            lineDic.update({'profile_id': item['_id']})
        except KeyError:
               lineDic.update({'profile_id': None})

        try:
            lineDic.update({'segment': item['recommendations']['segment']})
        except KeyError:
            lineDic.update({'segment': None})


        writer.writerow(lineDic)
file.close()
print('Finished creating profiles.csv')