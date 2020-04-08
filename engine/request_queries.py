from database.connection import createConnectionMysqlDBREC, createConnectionMysqlDB, createConnectionMongoDB
import datetime, ast, time, random
from sqlalchemy.sql import select
from sqlalchemy import desc
from engine.migrations.create_terms_table import Terms
from engine.migrations.create_trend_recommendations import Trend
from database.migrations.create_sessions_table import Sessions
from engine.migrations.create_homepage_recommendations import Homepage
from database.migrations.create_products_table import Products

recDB = createConnectionMysqlDBREC().connect()
dataDB = createConnectionMysqlDB().connect()


def get_term(profileId):
    profiles = dataDB.execute(
        select([Sessions.session_end], Sessions.profile_id == profileId, limit=1).order_by(desc(Sessions.session_end)))
    currentDate = None
    for profile in profiles:
        currentDate = datetime.datetime(profile[0].year, profile[0].month, 1)
    term = recDB.execute(select([Terms.id], Terms.term_date == currentDate))
    return term


def trend_recommendation(amount, profileId):
    print(profileId)
    print(createConnectionMongoDB())
    term = get_term(profileId)
    bestProducts = []
    for id in term:
        products = recDB.execute(
            select([Trend.product_id], Trend.term_id == id[0], order_by=[Trend.amount], limit=amount))
        for product in products:
            bestProducts.append(product[0])
    print(bestProducts)
    return bestProducts


def homepage_recommendation(profileId):
    term = get_term(profileId)
    productRecommendations = {}
    productCategories = []
    for id in term:
        products = recDB.execute(select([Homepage.category, Homepage.product_ids], Homepage.term_id == id[0]))
        for product in products:
            print(product)
            productItems = ast.literal_eval(product[1].replace('\r', ''))
            productRecommendations[product[0]] = productItems
    print(productRecommendations)


def collaborative_filter(profile_id):
    products = recDB.execute("SELECT product_id FROM collaborative_recommendations WHERE profile_id = '" + profile_id +
                             "'")
    product_lst = []
    for product in products:
        product_lst.append(list(product)[0].replace('\r', ''))
    return_lst = []
    try:
        for times in range(5):
            index = random.randrange(len(product_lst))
            return_lst.append(product_lst[index].split('"')[1])
            del product_lst[index]
        print(return_lst)
    except ValueError:
        products = recDB.execute("SELECT product_id FROM products LIMIT " + str(random.randrange(5000)) + ",1")
        for product in products:
            return_lst.append(list(product)[0].replace('\r', ''))
        print(return_lst)


collaborative_filter("5aca4c1ea1ade60001fc690f")
