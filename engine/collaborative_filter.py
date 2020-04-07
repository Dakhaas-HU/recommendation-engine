import mysql.connector
from mysql.connector import Error
import json
import time
t0 = time.time()


def write_data(file_name, data):
    with open(file_name, 'a+') as json_file:
        json_file.write(json.dumps(data))
        json_file.close()


def data_from_mysql(sql_select_query):
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def add_counter(user, profile, counter):
    if user[0] in counter and profile[0] in counter[user[0]]:
        counter[user[0]][profile[0]] += 1
    elif user[0] in counter:
        counter[user[0]][profile[0]] = 1
    else:
        counter[user[0]] = {}
        counter[user[0]][profile[0]] = 1
    return counter


def add_len(user, counter):
    if user[0] in counter and 'len' in counter[user[0]]:
        counter[user[0]]['len'] += 1
    else:
        counter[user[0]] = {}
        counter[user[0]]['len'] = 1


def compare_profiles(profile_lst, lst, counter):
    for user in profile_lst:
        add_len(user, counter)
        lst.remove(user)
        for profile in profile_lst:
            counter = add_counter(profile, user, counter)
            counter = add_counter(user, profile, counter)
    return lst, counter


def compare_users(lst, counter):
    for user in lst:
        profile_lst = []
        add_len(user, counter)
        lst.remove(user)
        for profile in lst:
            if user[1] == profile[1]:
                counter = add_counter(profile, user, counter)
                counter = add_counter(user, profile, counter)
                profile_lst.append(profile)
        lst, counter = compare_profiles(profile_lst, lst, counter)
    return counter


try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')
    # count_rows = int(data_from_mysql('select count(*) from previously_recommended')[0][0])
    # times = int(count_rows / 100000)
    # t, index, rownum, p_r = 0, '0', '100000', []
    # while t <= times:
        # p_r = compare_users(data_from_mysql('select profile_id, product_id from previously_recommended LIMIT ' + rownum
                                            # + ' OFFSET ' + index), {})
        # write_data('test.json', p_r)
        # index = str(int(index) + 100000)
        # t += 1
    compare_users(data_from_mysql('select profile_id, product_id from previously_recommended'), {})
    print(time.time() - t0)

except Error as e:
    print("Error reading data from MySQL table", e)
