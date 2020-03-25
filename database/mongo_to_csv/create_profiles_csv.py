from exporter.settings.database import createConnectionMongoDB
import csv
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("profiles.csv", "w+")

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