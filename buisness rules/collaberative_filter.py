import mysql.connector
from mysql.connector import Error


def data_from_mysql(table_name, query):
    sql_select_query = "select " + query + " from " + table_name
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def col_filter(records, counter):
    for row in records:
        if row[0] in counter:
            counter[row[0]] += [row[1]]
        else:
            counter[row[0]] = [row[1]]
    return counter


try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    lst = col_filter(data_from_mysql('viewed_before', 'profile_id, product_id'), {})
    lst = col_filter(data_from_mysql('previously_recommended', 'profile_id, product_id'), lst)
    print(lst)

except Error as e:
    print("Error reading data from MySQL table", e)
