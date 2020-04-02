import csv
import os

from dotenv import load_dotenv, find_dotenv

from database.connection import createConnectionMongoDB

load_dotenv(dotenv_path=find_dotenv(), verbose=True)
database = createConnectionMongoDB()
file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/sessions.csv", "w+", encoding="utf-8")

sessionsdata = database.sessions.find()
profilesdata = database.profiles.find()

print('Started creating profile dictionary')
profiledic = {}
for profile in profilesdata:
    try:
        buids = profile['buids']
        for buid in buids:
            profiledic[buid] = profile['_id']
    except KeyError:
        continue
print(len(profiledic))
with file:
    fnames = ['session_id', 'profile_id', 'session_start', 'session_end', 'os_family', 'browser_family',
              'device_brandutel', 'is_botutel', 'is_email_clientutel', 'is_mobileutel', 'is_pcutel', 'is_tabletutel', 'is_touchutel'
              ]
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter='#')
    print('Started creating sessions.csv')

    for item in sessionsdata:
        lineDic = {}
        try:
            lineDic.update({'session_id': item['_id']})
        except KeyError:
            lineDic.update({'session_id': None})

        try:
            lineDic.update({'profile_id': profiledic[''.join(item['buid'])]})
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
            lineDic.update({'os_family': item['user_agent']['os']['family']})
        except KeyError:
            lineDic.update({'os_family': None})

        try:
            lineDic.update({'browser_family': item['user_agent']['browser']['familiy']})
        except KeyError:
            lineDic.update({'browser_family': None})

        try:
            lineDic.update({'device_brandutel': item['user_agent']['device']['brand']})
        except KeyError:
            lineDic.update({'device_brandutel': None})

        try:
            lineDic.update({'is_botutel': item['user_agent']['flags']['is_bot']})
        except KeyError:
            lineDic.update({'is_botutel': None})

        try:
            lineDic.update({'is_email_clientutel': item['user_agent']['flags']['is_email_client']})
        except KeyError:
            lineDic.update({'is_email_clientutel': None})

        try:
            lineDic.update({'is_mobileutel': item['user_agent']['flags']['is_mobile']})
        except KeyError:
            lineDic.update({'is_mobileutel': None})

        try:
            lineDic.update({'is_pcutel': item['user_agent']['flags']['is_pc']})
        except KeyError:
            lineDic.update({'is_pcutel': None})

        try:
            lineDic.update({'is_tabletutel': item['user_agent']['flags']['is_tablet']})
        except KeyError:
            lineDic.update({'is_tabletutel': None})

        try:
            lineDic.update({'is_touchutel': item['user_agent']['flags']['is_touch_capable']})
        except KeyError:
            lineDic.update({'is_touchutel': None})

        writer.writerow(lineDic)
file.close()
print('Finished creating sessions.csv')