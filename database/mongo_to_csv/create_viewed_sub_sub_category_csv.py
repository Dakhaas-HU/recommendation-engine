from database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("./csv/viewed_sub_sub_category.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'sub_sub_gategory_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_sub_sub_gategory.csv')

    for item in data:
        try:
            sub_sub_gategorys = item['preferences']['sub_sub_category']
            for sub_sub_gategory in sub_sub_gategorys:
                lineDic = {}
                print(sub_sub_gategory)
                try:
                    lineDic.update({'session_id': item['_id']})
                except KeyError:
                    lineDic.update({'session_id': None})

                try:
                    lineDic.update({'views': sub_sub_gategory['views']})
                except KeyError:
                    lineDic.update({'views': None})
                except TypeError:
                    lineDic.update({'views': None})

                try:
                    lineDic.update({'sub_sub_gategory_name': sub_sub_gategory})
                except KeyError:
                    lineDic.update({'sub_sub_gategory_name': None})

                writer.writerow(lineDic)
        except KeyError:
            continue
file.close()
print('Finished creating viewed_sub_sub_gategory.csv')