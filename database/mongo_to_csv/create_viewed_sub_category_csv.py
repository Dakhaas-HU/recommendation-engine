import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/sub_category.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'sub_gategory_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames, quoting='#')
    print('Started creating viewed_sub_gategory.csv')

    for item in data:
        try:
            sub_gategorys = item['preferences']['sub_category']
            for sub_gategory in sub_gategorys:
                lineDic = {}
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': sub_gategory['views']})
                except KeyError:
                    lineDic.update({'views': None})
                except TypeError:
                    lineDic.update({'views': None})

                try:
                    lineDic.update({'sub_gategory_name': sub_gategory})
                except KeyError:
                    lineDic.update({'sub_gategory_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_sub_gategory.csv')