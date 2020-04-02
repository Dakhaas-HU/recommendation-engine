import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    query = "session_id, browser_family, device_brand, os_family, is_bot"
    sql_select_Query = "select " + query + " from sessions"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        if row[3] != '':
            print(row)

except Error as e:
    print("Error reading data from MySQL table", e)
