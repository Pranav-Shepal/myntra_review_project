import pandas as pd
from urllib.parse import quote_plus
from database_connect import mongo_operation as mongo
import os,sys
from src.constants import *
from src.exception import CustomException


class MongoIO:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoIO, cls).__new__(cls)
            cls._instance.__init_singleton(*args, **kwargs)
        return cls._instance

    def __init_singleton(self):
        # Ensure password is properly encoded
        password = "Pranav@07"
        encoded_password = quote_plus(password)
        mongo_db_url = f"mongodb+srv://pranav_shepal:{encoded_password}@cluster0.wblerzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # "mongodb+srv://pranav_shepal:<db_password>@cluster0.wblerzp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        if not mongo_db_url:
            raise Exception("MongoDB URL is not set.")
        
        self.mongo_ins = mongo(client_url=mongo_db_url, database_name=MONGO_DATABASE_NAME)
    
    def store_reviews(self,product_name:str,reviews:pd.DataFrame):
        try:
            collection_name=product_name.replace(" ","_")
            self.mongo_ins.bulk_insert(reviews,collection_name)
        
        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self,product_name:str):
        try:
            collection_name=product_name.replace(" ","_")
            data=self.mongo_ins.find(collection_name)
            return data
        except Exception as e:
            raise CustomException(e, sys)
        