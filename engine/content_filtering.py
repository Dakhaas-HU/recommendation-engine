import mysql.connector


# Dit haalt de product data uit de database met een aanpasbaren query.
def queryproductdata(table_name, query, limit1, limit2, limit3, limit4, limit5, limit6, limit7, limit8, limit):
    sql_select_query = 'select ' + query + ' from ' + table_name + ' where ' + limit1 + limit2 + limit3 + \
                       limit4 + limit5 + limit6 + limit7 + limit8 + limit
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


# Maakt een lijst met alle condities waar de query aan moet voldoen.
def contentdata(product):
    lst = ['', '', '', '', '', '', '']
    nrs = [13, 1, 10, 3, 19, 21, 20]
    koloms = [' availablity = ', ' brand = ', ' sub_sub_category = ', ' color = ', ' type = ',
              ' type_hair_color = ', ' type_hair_care = ']
    for nr in nrs:
        if (product[0])[nr] is not '':
            if lst == ['', '', '', '', '', '', '']:
                lst[nrs.index(nr)] = (koloms[nrs.index(nr)] + '"' + (product[0])[nr] + '" ')
            else:
                lst[nrs.index(nr)] = 'and' + koloms[nrs.index(nr)] + '"' + (product[0])[nr] + '" '
    return lst


# Main script, data van het bekeken product word opgehaald
# en maakt de querys die opzoek gaan naar vergelijkbare producten.
# Zet de recommendations in een list.
def content_filter(count, productid):
    querylimits = contentdata(queryproductdata('products', '*', 'product_id = "' + productid + '"', '', '', '', '', '',
                                               '', '', ' limit 1'))
    product = []
    recommendations = []
    limitcount = 6
    while not product:
        product = queryproductdata('products', 'product_id', querylimits[0], querylimits[1], querylimits[2],
                                   querylimits[3],
                                   querylimits[4], querylimits[5], querylimits[6], 'and product_id != "'
                                   + productid + '"', ' limit ' + str(count))
        if not product:
            limitcount -= 1
            querylimits[limitcount] = ''
    for id in product:
        recommendations.append(id[0])
    return recommendations


connection = mysql.connector.connect(host='78.46.250.83',
                                     database='huwebshop',
                                     user='groupproject',
                                     password='Bierkeet42069!')
