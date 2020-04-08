import mysql.connector
from mysql.connector import Error
import json
import csv
import os
counter, o_user_lst = {}, []


def write_csv(data):
    file = open("csv/orders_C.csv", "w+", encoding="utf-8")
    with file:
        fnames = ['user_id', 'profile_id', 'compatibility'
                  ]
        writer = csv.DictWriter(file, fieldnames=fnames, delimiter='#')
        print('Started creating order_C.csv')
        for user in data:
            for profile in data[user]:
                lineDic = {}
                lineDic.update({'user_id': user})
                lineDic.update({'profile_id': profile})
                lineDic.update({'compatibility': data[user][profile]})
                writer.writerow(lineDic)
    file.close()
    print('Finished creating order_C.csv')


"""
# Schrijft data naar een json bestand
def write_data(file_name, data):
    with open(file_name, 'w+') as json_file:
        json_file.write(json.dumps(data))
        json_file.close()
"""

# Haalt data op van de SQL server
def data_from_mysql(sql_select_query):
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


# Voegt punten toe aan profile_id's
def add_counter(user, profile):
    if user[0] in counter and profile[0] in counter[user[0]]:
        counter[user[0]][profile[0]] += 1
    elif user[0] in counter:
        counter[user[0]][profile[0]] = 1
    else:
        counter[user[0]] = {}
        counter[user[0]][profile[0]] = 1


# Kijkt of profielen hetzelfde zijn
def compare_profiles(profile_lst, lst):
    for user in profile_lst:
        lst.remove(user)
        for profile in profile_lst:
            add_counter(profile, user)
            add_counter(user, profile)
    return lst


def compare_user_order(users):
    for user in users:
        if user[0] not in o_user_lst:
            o_user_lst.append(user[0])
        profile_lst = []
        users.remove(user)
        for profile in users:
            if user[1] == profile[1]:
                profile_lst.append(profile)
                add_counter(user, profile)
                add_counter(profile, user)
        users = compare_profiles(profile_lst, users)
    del users


def compare_user_viewed_before(users):
    for user in users:
        if user[0] not in o_user_lst:
            profile_lst = []
            users.remove(user)
            for profile in users:
                if user[1] == profile[1]:
                    profile_lst.append(profile)
                    add_counter(user, profile)
                    add_counter(profile, user)
            users = compare_profiles(profile_lst, users)


try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    compare_user_order(data_from_mysql("SELECT profile_id, product_id FROM orders INNER JOIN sessions ON orders.session_id = sessions.session_id AND sessions.profile_id != ''"))
    write_csv(counter)

    """write_data('order_data.json', counter)
    counter = {}
    compare_user_viewed_before(data_from_mysql("SELECT * FROM viewed_before"))
    write_data('viewed_before_data.json', counter)"""

except Error as e:
    print("Error reading data from MySQL table", e)
