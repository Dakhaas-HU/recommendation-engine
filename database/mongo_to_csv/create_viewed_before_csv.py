from exporter.settings.database import createConnectionMongoDB
import csv
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("viewed_before.csv", "w+")

data = database.profiles.find()

with file:
    fnames = ['profiles_id', 'product_id'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_before.csv')

    for item in data:
        product_ids = item['recommendations']['viewed_before']
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
print('Finished creating viewed_before')