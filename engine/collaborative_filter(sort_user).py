import mysql.connector
from mysql.connector import Error
import json
counter = {}


def write_data(file_name, data):
    with open(file_name, 'w+') as file:
        file.write(json.dumps(data))
        file.close()


def data_from_mysql(sql_select_query):
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def compare_users(lst):
    for user in lst:
        if user in counter:
            counter[user[0]] += [user[1]]
        else:
            counter[user[0]] = [user[1]]


try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    count_rows = int(data_from_mysql('select count(*) from previously_recommended')[0][0])
    times = int(count_rows / 100000)
    t, index, rownum = 0, '0', '100000'
    while t <= times:
        compare_users(data_from_mysql('select profile_id, product_id from previously_recommended LIMIT ' + rownum +
                                      ' OFFSET ' + index))
        index = str(int(index) + 100000)
        t += 1

except Error as e:
    print("Error reading data from MySQL table", e)
