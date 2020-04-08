import mysql.connector
from mysql.connector import Error
import csv
import os
counter, products_lst = {}, {}


def write_csv(data):
    file = open(os.path.dirname(os.path.abspath(__file__)) + "/csv/order_C.csv", "w+", encoding="utf-8")
    with file:
        fnames = ['profile_id', 'product_id', 'compatibility'
                  ]
        writer = csv.DictWriter(file, fieldnames=fnames, delimiter='#')
        print('Started creating order_C.csv')
        for user in data:
            lst = []
            for profile in data[user]:
                for product in products_lst[profile]:
                    if product not in products_lst[user] and product not in lst:
                        lst.append(product)
                        lineDic = {}

                        lineDic.update({'profile_id': user})

                        lineDic.update({'product_id': str(product)})

                        lineDic.update({'compatibility': data[user][profile]})

                        writer.writerow(lineDic)
    file.close()
    print('Finished creating order_C.csv')


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


def append_products(profile, products):
    if profile in products_lst:
        products_lst[profile] += [products]
    else:
        products_lst[profile] = [products]


def compare_user_order(users):
    for user in users:
        append_products(user[0], user[1])
        profile_lst = []
        users.remove(user)
        for profile in users:
            if user[1] == profile[1]:
                profile_lst.append(profile)
                append_products(profile[0], profile[1])
                add_counter(user, profile)
                add_counter(profile, user)
        users = compare_profiles(profile_lst, users)
    del users


try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    compare_user_order(data_from_mysql("SELECT profile_id, product_id FROM orders INNER JOIN sessions ON orders.session_id = sessions.session_id AND sessions.profile_id != ''"))
    write_csv(counter)

except Error as e:
    print("Error reading data from MySQL table", e)
