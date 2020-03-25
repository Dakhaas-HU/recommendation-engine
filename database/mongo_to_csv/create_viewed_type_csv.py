from exporter.settings.database import createConnectionMongoDB
import csv

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("viewed_type.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'type_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_type.csv')

    for item in data:
        types = item['preferences']['type']
        for type in types:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': type['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'type_name': type})
            except KeyError:
                lineDic.update({'type_name': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_type.csv')