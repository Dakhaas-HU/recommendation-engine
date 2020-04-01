import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/sessions.csv", "w+", encoding="utf-8")

data = database.sessions.find()

with file:
    fnames = ['session_id', 'profile_id', 'session_start', 'session_end', 'os_family', 'browser_family',
              'device_brandutel', 'is_botutel', 'is_email_clientutel', 'is_mobileutel', 'is_pcutel', 'is_tabletutel', 'is_touchutel'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames)
    print('Started creating sessions.csv')

    for item in data:
        lineDic = {}
        try:
            lineDic.update({'session_id': item['_id']})
        except KeyError:
            lineDic.update({'session_id': None})

        try:
            # TODO: Redo this, use an array for this.
            profile = database.profiles.find_one({'buids': item['buid']})
            lineDic.update({'profile_id': profile['_id']})
        except KeyError:
            lineDic.update({'profile_id': None})
        except TypeError:
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