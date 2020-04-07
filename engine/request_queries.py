from database.connection import createConnectionMysqlDBREC
import datetime
from sqlalchemy.sql import select
from engine.migrations.create_terms_table import Terms
from engine.migrations.create_trend_recommendations import Trend

database = createConnectionMysqlDBREC().connect()


def trend_recommendation(amount):
    currentDate = datetime.datetime(2017, 1, 1)
    term = database.execute(select([Terms.id], Terms.term_date == currentDate))
    bestProducts = []
    for id in term:
        products = database.execute(select([Trend.product_id], Trend.term_id == id[0], order_by=[Trend.amount], limit=amount))
        for product in products:
            bestProducts.append(product[0])
    print(bestProducts)
    return bestProducts
