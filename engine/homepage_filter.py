from database.connection import createConnectionMysqlDB, createConnectionMysqlDBREC, createConnectionMongoDB
import os, csv
from sqlalchemy.sql import select
from engine.migrations.create_trend_recommendations import Trend
from engine.migrations.create_terms_table import Terms
from database.migrations.create_products_table import Products

recDB = createConnectionMysqlDBREC().connect()
dataDB = createConnectionMysqlDB().connect()
mongoDB = createConnectionMongoDB().huwebshop


def prepproduct( p):
    """ This helper function flattens and rationalizes the values retrieved
    for a product block element. """
    r = {}
    r['name'] = p['name']
    r['price'] = p['price']['selling_price']
    r['price'] = str(r['price'])[0:-2] + ",-" if r['price'] % 100 == 0 else str(r['price'])[0:-2] + "," + str(
        r['price'])[-2:]
    if r['price'][0:1] == ",":
        r['price'] = "0" + r['price']
    if p['properties']['discount'] is not None:
        r['discount'] = p['properties']['discount']
    r['smallimage'] = ""  # TODO: replace this with actual images!
    r['bigimage'] = ""  # TODO: replace this with actual images!
    r['id'] = p['_id']
    return r


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
            if len(productRecommendation[category]) != 4:
                getAmount = 4 - len(productRecommendation[category])
                newRecProds = dataDB.execute(select([Products.product_id], Products.category == category, limit=(getAmount * 2)))
                for recProduct in newRecProds:
                    if recProduct[0] not in productRecommendation[category] and len(productRecommendation[category]) != 4:
                        productRecommendation[category].append(recProduct[0])
            queryfilter = {"_id": {"$in": productRecommendation[category]}}
            querycursor = mongoDB.products.find(queryfilter, ['name', 'price.selling_price', 'properties.discount', 'images'])
            resultlist = list(map(prepproduct, list(querycursor)))
            writer.writerow({'term_id': term[0], 'category': category, 'product_ids': str(resultlist)})

    print("Finished creating homepage filter data")


homepage_filter()
