import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/viewed_category.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'category_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter='#')
    print('Started creating viewed_category.csv')

    for item in data:
        try:
            categories = item['preferences']['category']
            for category in categories:
                lineDic = {}
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': categories[category]['views']})
                except KeyError:
                    lineDic.update({'views': None})

                try:
                    lineDic.update({'category_name': category})
                except KeyError:
                    lineDic.update({'category_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_category.csv')