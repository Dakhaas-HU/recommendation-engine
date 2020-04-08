from database.connection import createConnectionMysqlDBREC, createConnectionMysqlDB, createConnectionMongoDB
import datetime, ast, time
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


homepage_recommendation("5ada1302fd52a800013a999e")