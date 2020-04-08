import mysql.connector


def queryproductdata(table_name, query, limit1):
    sql_select_query = 'select ' + query + ' from ' + table_name + ' where product_id = "' + limit1 + '"'
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def discount_filter(recommendations):
    sortedrecommendations = []
    for product in recommendations:
        discount = queryproductdata('products', 'discount', product)
        if (discount[0])[0] is not '':
            sortedrecommendations.insert(0, product)
        else:
            sortedrecommendations.append(product)
    return sortedrecommendations


connection = mysql.connector.connect(host='78.46.250.83',
                                     database='huwebshop',
                                     user='groupproject',
                                     password='Bierkeet42069!')
