import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='78.46.250.83',
                                         database='huwebshop',
                                         user='groupproject',
                                         password='Bierkeet42069!')

    query = "session_id, "
    sql_select_Query = "select " + query + " from sessions"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

except Error as e:
    print("Error reading data from MySQL table", e)