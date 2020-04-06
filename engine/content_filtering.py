import mysql.connector
from mysql.connector import Error
query = "product_id, category, color"

try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    sql_select_Query = "select " + query + " from products"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    f_names = query.split(', ')
    counter, t = {}, 0
    for row in records:
        t += 1
        table_name = row[1] + row[2]
        if table_name in counter:
            counter[table_name] += [row[0]]
        else:
            counter[table_name] = [row[0]]

    for row in counter:
        print(row, counter[row])

except Error as e:
    print("Error reading data from MySQL table", e)