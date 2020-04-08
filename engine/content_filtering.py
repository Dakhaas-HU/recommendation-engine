import mysql.connector


def queryproductdata(table_name, query, limit1, limit2, limit3, limit4, limit5, limit6, limit7, limit8, limit):
    sql_select_query = 'select ' + query + ' from ' + table_name + ' where ' + limit1 + limit2 + limit3 + \
                       limit4 + limit5 + limit6 + limit7 + limit8 + limit
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def contentdata(product):
    lst = ['', '', '', '', '', '', '']
    nrs = [13, 1, 10, 3, 19, 21, 20]
    koloms = ['availablity =', 'and brand =', 'and sub_sub_category =', 'and color =', 'and type =',
              'and type_hair_color =', 'and type_hair_care =']
    for nr in nrs:
        if (product[0])[nr] is not '':
            lst[nrs.index(nr)] = koloms[nrs.index(nr)] + ' "' + (product[0])[nr] + '" '
    return lst


def recommend_query(count, productid):
    querylimits = contentdata(queryproductdata('products', '*', 'product_id = "' + productid + '"', '', '', '', '', '',
                                               '', '', ' limit 1'))
    print(querylimits)
    product = []
    limitcount = 6
    while not product:
        product = queryproductdata('products', '*', querylimits[0], querylimits[1], querylimits[2], querylimits[3],
                                   querylimits[4], querylimits[5], querylimits[6], 'and product_id != "'
                                   + productid + '"', ' limit ' + str(count))
        if not product:
            limitcount -= 1
            querylimits[limitcount] = ''
    return product


connection = mysql.connector.connect(host='78.46.250.83',
                                     database='huwebshop',
                                     user='groupproject',
                                     password='Bierkeet42069!')


print(recommend_query(5, '02112'))
