import mysql.connector
from mysql.connector import Error
import json
lst = {}


def data_from_mysql(table_name, query):
    sql_select_query = "select " + query + table_name
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def col_filter(records, counter):
    global lst
    for row in records:
        if row[0] in counter:
            counter[row[0]] += [row[1]]
        else:
            counter[row[0]] = [row[1]]
    lst.update(counter)


try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    count_rows = int(data_from_mysql(' from previously_recommended', 'COUNT(*)')[0][0])
    times = int(count_rows / 1000000)
    col_filter(data_from_mysql(' from viewed_before', 'profile_id, product_id'), {})
    t, index, rownum = 0, '0', '1000000'
    while t <= times:
        col_filter(data_from_mysql(' from previously_recommended LIMIT ' + rownum + ' OFFSET ' + index, 'profile_id, product_id'), {})
        index = str(int(index) + 1000000)
        t += 1

    col_filter(data_from_mysql(' from orders', 'session_id, product_id'), {})

    with open('test.json', 'w+') as file:
        file.write(json.dumps(lst))
        file.close()

except Error as e:
    print("Error reading data from MySQL table", e)
