from exporter.settings.database import createConnectionMongoDB
import csv
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("order.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['product_id', 'session_id'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating order.csv')

    for item in data:
        products = item['order']['products']
        for id in products:
            lineDic = {}
            print(id)
            try:
                lineDic.update({'session_id': item['_id']})
            except KeyError:
                lineDic.update({'session_id': None})

            try:
                lineDic.update({'product_id': id['id']})
            except KeyError:
                lineDic.update({'product_id': None})


            writer.writerow(lineDic)
file.close()
print('Finished creating order.csv')