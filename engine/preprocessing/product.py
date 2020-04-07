import mysql.connector
from mysql.connector import Error


def queryproductdata(table_name, query, limit1, limit2, limit3):
    sql_select_query = 'select ' + query + ' from ' + table_name + ' where ' + limit1 + ' and ' + limit2 + ' and ' +\
                       limit3
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    return records


def update_value(value, kolom,  limit1):
    if value is None:
        value = 'NULL'
        sql_update_color = 'update products set ' + kolom + ' = ' + value + ' where ' + limit1.replace('"', '\"')
    else:
        sql_update_color = 'update products set ' + kolom + ' =  "' + value.capitalize() + '" where ' + \
                           limit1.replace('"', '\"')
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
colorset = {'color_set'}
for color in queryproductdata('products', 'color', 'color != ""', 'color != ""', 'color != ""'):
    colorset.add(color[0].lower())

# create sub_sub_category set
categoryset = {'category'}
for category in queryproductdata('products', 'sub_sub_category', 'sub_sub_category != ""', 'sub_sub_category != ""',
                                 'sub_sub_category != ""'):
    categoryset.add(category[0].lower())

# update color by product_id
print('updating color...')
for product in queryproductdata('products', 'product_id', 'color = ""', 'color = ""', 'color = ""'):
    update_value(search_data(product[0], colorset), 'color', 'product_id = """' + product[0].replace('"', '') + '"""')

# update color by name
for name in queryproductdata('products', 'name', 'color = ""', 'name != ""', 'name != ""'):
    update_value(search_data(name[0], colorset), 'color', 'name = """' + name[0].replace('"', '') + '"""')

# update sub_sub_category by name
print('updating sub_sub_category...')
for name in queryproductdata('products', 'name', 'sub_sub_category = ""', 'name != ""', 'name != ""'):
    update_value(search_data(name[0], categoryset), 'sub_sub_category', 'name = """' + name[0].replace('"', '') + '"""')

# update sub_sub_category by description
for description in queryproductdata('products', 'description', 'sub_sub_category = ""', 'description != ""',
                                    'description != ""'):
    update_value(search_data(description[0], categoryset), 'sub_sub_category', 'description = """'
                 + description[0].replace('"', '') + '"""')
