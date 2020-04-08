from database.connection import createConnectionMysqlDBREC, createConnectionMysqlDB, createConnectionMongoDB
import datetime
from sqlalchemy.sql import select
from sqlalchemy import desc
from engine.migrations.create_terms_table import Terms
from engine.migrations.create_trend_recommendations import Trend
from database.migrations.create_sessions_table import Sessions

recDB = createConnectionMysqlDBREC().connect()
dataDB = createConnectionMysqlDB().connect()


def trend_recommendation(amount, profileId):
    print(profileId)
    print(createConnectionMongoDB())
    profiles = dataDB.execute(select([Sessions.session_end], Sessions.profile_id == profileId, limit=1).order_by(desc(Sessions.session_end)))
    currentDate = None
    for profile in profiles:
        currentDate = datetime.datetime(profile[0].year, profile[0].month, 1)
    term = recDB.execute(select([Terms.id], Terms.term_date == currentDate))
    bestProducts = []
    for id in term:
        products = recDB.execute(select([Trend.product_id], Trend.term_id == id[0], order_by=[Trend.amount], limit=amount))
        for product in products:
            bestProducts.append(product[0])
    print(bestProducts)
    return bestProducts

