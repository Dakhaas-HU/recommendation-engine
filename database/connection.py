from pymongo import MongoClient
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os

def createConnectionMongoDB():
    if os.getenv("DB_USE_AUTH") == 'TRUE':
        return MongoClient(host=os.getenv("MONGODB_HOST"), port=int(os.getenv("MONGODB_PORT")),
                           authSource=os.getenv("MONGODB_AUTH_DB"),
                           username=os.getenv("MONGODB_USERNAME"), password=os.getenv("MONGODB_PASSWORD"),
                           database=os.getenv("MONGODB_DATABASE"))
    else:
        return MongoClient(host=os.getenv("MONGODB_HOST"), port=int(os.getenv("MONGODB_PORT")),
                           database=os.getenv("MONGODB_DATABASE"))


def createConnectionMysqlDB():
    load_dotenv()
    if os.getenv("SQLDB_USE_AUTH") == 'True':
        db_uri = 'mysql+pymysql://' + os.getenv('SQLDB_USERNAME') + ':' + os.getenv('SQLDB_PASSWORD') + '@' + os.getenv(
            'SQLDB_HOST') + '/' + os.getenv('SQLDB_DATABASE')
        return create_engine(db_uri)
    else:
        db_uri = 'mysql+pymysql://' + os.getenv('SQLDB_USERNAME') + ':@' + os.getenv('SQLDB_HOST') + '/' + os.getenv(
            'SQLDB_DATABASE')
        return create_engine(db_uri)
