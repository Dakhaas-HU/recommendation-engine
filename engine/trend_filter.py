import csv
import datetime
import os
import subprocess

from sqlalchemy import Date, extract, join
from sqlalchemy.sql import select, insert
from sqlalchemy.orm import sessionmaker

from database.connection import createConnectionMysqlDB, createConnectionMysqlDBREC
from database.migrations.create_products_table import Products
from database.migrations.create_sessions_table import Sessions
from database.migrations.create_order_table import Order
from engine.migrations.create_terms_table import Terms
from engine.migrations.create_products_table import Products as ProductsREC

huwebshop = createConnectionMysqlDB().connect()
huRec = createConnectionMysqlDBREC().connect()


def createTerms():
    # Get all dates from sessions, only the year and month because the term is only 1 month long
    sessions = huwebshop.execute(select([extract('year', Sessions.session_end.cast(Date)),
                                         extract('month', Sessions.session_end.cast(Date))]).distinct())
    terms = []
    # Loop through all the dates and transform them to datetime objects
    for date in sessions:
        dateTerm = datetime.datetime(date[0], date[1], 1)
        terms.append(dateTerm)
    terms.sort()
    # Insert the terms
    for item in terms:
        huRec.execute(insert(Terms, values={"term_date": item}))


def createProducts():
    file = open(os.path.dirname(os.path.abspath(__file__)) + '/csv/products.csv', "w+", encoding="utf-8")
    fnames = ['product_id']
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter="#")
    products = huwebshop.execute(select([Products.product_id]))
    for product in products:
        writer.writerow({'product_id': product[0]})
    subprocess.call(['./shscripts/import_csv.sh'])


def createRec():
    orders = huwebshop.execute(
        "SELECT * FROM orders INNER JOIN sessions ON orders.session_id = sessions.session_id")
    trendRec = {}
    for order in orders:
        date = datetime.datetime(order[4].year, order[4].month, 1)
        term = huRec.execute(select([Terms.id], Terms.term_date == date))
        for item in term:
            if item[0] in trendRec:
                if order[1] in trendRec[item[0]]:
                    trendRec[item[0]].update(
                        {order[1]: [order[1].replace('\r', ''), item[0], trendRec[item[0]].get(order[1])[2] + 1]})
                else:
                    newTrend = {order[1]: [order[1].replace('\r', ''), item[0], 1]}
                    trendRec[item[0]].update(newTrend)
            else:
                trendRec.update({item[0]: {order[1]: [order[1].replace('\r', ''), item[0], 1]}})
    trendIds = huRec.execute(select([Terms.id]))
    file = open(os.path.dirname(os.path.abspath(__file__)) + '/csv/trend_recommendations.csv', "w+", encoding="utf-8")
    fnames = ['product_id', 'term_id', 'amount']
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter="#")
    for id in trendIds:
        trendProducts = trendRec.get(id[0])
        trendProductKeys = trendProducts.keys()
        for key in trendProductKeys:
            trendCount = trendProducts.get(key)
            writer.writerow({'product_id': trendCount[0], 'term_id': trendCount[1], 'amount': trendCount[0]})


createRec()
