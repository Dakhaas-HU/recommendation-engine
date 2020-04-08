from database.connection import createConnectionMysqlDB, createConnectionMysqlDBREC
import os, csv
from sqlalchemy.sql import select
from engine.migrations.create_trend_recommendations import Trend
from engine.migrations.create_terms_table import Terms
from database.migrations.create_products_table import Products

recDB = createConnectionMysqlDBREC().connect()
dataDB = createConnectionMysqlDB().connect()


def homepage_filter():
    print("Started creating homepage filter data")
    currentTerm = recDB.execute(select([Terms.id]))
    productRecommendation = {}
    file = open(os.path.dirname(os.path.abspath(__file__)) + '/csv/homepage_recommendations.csv', "w+", encoding="utf-8")
    fnames = ['term_id', 'category', 'product_ids']
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter="#")
    for term in currentTerm:
        productsInTerm = recDB.execute(select([Trend.product_id], Trend.term_id == term[0], order_by=[Trend.amount]))
        for product in productsInTerm:
            productCategory = dataDB.execute(select([Products.category], Products.product_id == product[0]))
            for category in productCategory:
                if category[0] in productRecommendation:
                    if product[0] not in productRecommendation[category[0]] and len(productRecommendation[category[0]]) < 4:
                        productRecommendation[category[0]].append(product[0])
                else:
                    productRecommendation.update({category[0]: [product[0]]})
        for category in productRecommendation:
            writer.writerow({'term_id': term[0], 'category': category, 'product_ids': str(productRecommendation[category])})

    print("Finished creating homepage filter data")


homepage_filter()
