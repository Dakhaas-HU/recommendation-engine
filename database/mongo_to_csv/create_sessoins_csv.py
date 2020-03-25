from recommendation_engine.database.connection import createConnectionMongoDB
import csv
from dotenv import load_dotenv, find_dotenv
load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
# TODO: Vragen waarom hiervoor geen path en bij sessions wel?
file = open("sessions.csv", "w+")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'profile_id', 'session_start', 'session_end', 'os_family', 'browser_family',
              'device_brandutel', 'is_botutel', 'is_email_clientutel', 'is_mobileutel', 'is_pcutel', 'is_tabletutel', 'is_touchutel'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating sessions.csv')

    for item in data:
        lineDic = {}
        print(item)
        try:
            lineDic.update({'session_id': item['_id']})
        except KeyError:
            lineDic.update({'session_id': None})

        try:
            lineDic.update({'profile_id': item['profile_id']})
        except KeyError:
            lineDic.update({'profile_id': None})

        try:
            lineDic.update({'session_start': item['session_start']})
        except KeyError:
            lineDic.update({'session_start': None})

        try:
            lineDic.update({'session_end': item['session_end']})
        except KeyError:
            lineDic.update({'session_end': None})

        try:
            lineDic.update({'os_family': item['os']['family']})
        except KeyError:
            lineDic.update({'os_family': None})

        try:
            lineDic.update({'browser_family': item['browser']['family']})
        except KeyError:
            lineDic.update({'browser_family': None})

        try:
            lineDic.update({'device_brandutel': item['device']['brand']})
        except KeyError:
            lineDic.update({'device_brandutel': None})

        try:
            lineDic.update({'is_botutel': item['flags']['is_bot']})
        except KeyError:
            lineDic.update({'is_botutel': None})

        try:
            lineDic.update({'is_email_clientutel': item['flags']['is_email_clientutel']})
        except KeyError:
            lineDic.update({'is_email_clientutel': None})

        try:
            lineDic.update({'is_mobileutel': item['flags']['is_mobile']})
        except KeyError:
            lineDic.update({'is_mobileutel': None})

        try:
            lineDic.update({'is_pcutel': item['flags']['is_pc']})
        except KeyError:
            lineDic.update({'is_pcutel': None})

        try:
            lineDic.update({'is_tabletutel': item['flags']['is_tablet']})
        except KeyError:
            lineDic.update({'is_tabletutel': None})

        try:
            lineDic.update({'is_touchutel': item['flags']['is_touch_capable']})
        except KeyError:
            lineDic.update({'is_touchutel': None})

        writer.writerow(lineDic)
file.close()
print('Finished creating sessions.csv')