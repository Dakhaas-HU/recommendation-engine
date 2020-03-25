from exporter.settings.database import createConnectionMongoDB
import csv

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("viewed_promos.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'promos_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_promos.csv')

    for item in data:
        promos = item['preferences']['promos']
        for promo in promos:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': promo['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'promos': promo})
            except KeyError:
                lineDic.update({'promos': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_product_type.csv')