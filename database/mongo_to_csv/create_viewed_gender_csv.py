from exporter.settings.database import createConnectionMongoDB
import csv

database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("viewed_gender.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'views', 'gender_name'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating viewed_gender.csv')

    for item in data:
        genders = item['preferences']['gender']
        for gender in genders:
            lineDic = {}
            print(item)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'views': gender['views']})
            except KeyError:
                lineDic.update({'views': None})

            try:
                lineDic.update({'gender_name': gender})
            except KeyError:
                lineDic.update({'gender_name': None})

            writer.writerow(lineDic)
file.close()
print('Finished creating viewed_gender.csv')