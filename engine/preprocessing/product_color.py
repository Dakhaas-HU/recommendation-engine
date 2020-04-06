import mysql.connector
from mysql.connector import Error


def queryproductdata(table_name, query, limit1, limit2, limit3):
    sql_select_query = 'select ' + query + ' from ' + table_name + ' where ' + limit1 + ' and ' + limit2 + ' and ' + limit3
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def update_color(new_color, limit1):
    sql_update_color = 'update products set ' + new_color + ' where ' + limit1
    cursor = connection.cursor()
    cursor.execute(sql_update_color)


def search_data(item, product_set):
    for set_item in product_set:
        if set_item in item.lower():
            return set_item


connection = mysql.connector.connect(host='78.46.250.83',
                                     database='huwebshop',
                                     user='groupproject',
                                     password='Bierkeet42069!')

# create color set
colorset = {'kleur'}
for color in queryproductdata('products', 'color', 'color != ""', 'color != ""', 'color != ""'):
    colorset.add(color[0].lower())

# create sub_sub_category set
categoryset = {'category'}
for category in queryproductdata('products', 'sub_sub_category', 'sub_sub_category != ""', 'sub_sub_category != ""',
                                 'sub_sub_category != ""'):
    categoryset.add(category[0].lower())

# update color by product_id
for product in queryproductdata('products', 'product_id', 'color = ""', 'color = ""', 'color = ""'):
    update_color('color = ' + str(search_data(product[0], colorset)), 'product_id = ' + '"' + product[0] + '"')

# update color by name
for name in queryproductdata('products', 'name', 'color = ""', 'name != ""', 'name != ""'):
    update_color('color = ' + str(search_data(name[0], colorset)), 'name = "' + name[0] + '"')

# update sub_sub_category by name
for name in queryproductdata('products', 'name', 'sub_sub_category = ""', 'name != ""', 'name != ""'):
    search_data(name, categoryset)

# update sub_sub_category by description
for description in queryproductdata('products', 'description', 'sub_sub_category = ""', 'description != ""', 'description != ""'):
    search_data(description, categoryset)
