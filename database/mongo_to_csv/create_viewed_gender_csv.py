import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/viewed_gender.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'gender_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_gender.csv')

    for item in data:
        try:
            genders = item['preferences']['gender']
            for gender in genders:
                lineDic = {}
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': genders[gender]['views']})
                except KeyError:
                    lineDic.update({'views': None})

                try:
                    lineDic.update({'gender_name': gender})
                except KeyError:
                    lineDic.update({'gender_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_gender.csv')