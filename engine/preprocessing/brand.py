from database.connection import createConnectionMysqlDB
from sqlalchemy.sql import select, update
from sqlalchemy import distinct
from database.migrations.create_products_table import Products

session = createConnectionMysqlDB().connect()

brands = []
for brand in session.execute(select([distinct(Products.brand)])):
    if brand[0]:
        brands.append(brand[0])


for product in session.execute(select([Products]).where(Products.brand == '').where(Products.name != '')):
    productNameWords = product[6].split(" ")
    for word in productNameWords:
        if word in brands:
            brand = brands[brands.index(word)]
            session.execute(update(Products).where(Products.product_id ==product[0]).values(brand=brand))
            break
