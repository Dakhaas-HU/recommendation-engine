from exporter.settings.database import createConnectionMongoDB
import csv

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("viewed_category.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'category_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_category.csv')

    for item in data:
        categorys = item['preferences']['category']
        for category in categorys:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': category['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'brand_name': category})
            except KeyError:
                lineDic.update({'brand_name': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_category.csv')