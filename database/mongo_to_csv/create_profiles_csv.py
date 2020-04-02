import csv
import os

from database.connection import createConnectionMongoDB
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/profiles.csv", "w+", encoding="utf-8")

data = database.profiles.find()

with file:
    fnames = ['profile_id', 'segment'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames, quoting='#')
    print('Started creating profiles.csv')

    for item in data:
        lineDic = {}
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