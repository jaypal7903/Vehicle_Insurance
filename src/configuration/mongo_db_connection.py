import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# load the certificate authority file to avoid timeout errors when connecting to mongodb
ca = certifi.where()

class MongoDBClient :
    """
    MongoDBClient is the responsible for establishing connection to the mongoDB database.

    Attributes:
    -----------
    client : MongoDBClient 
        A shared MongoDBClient instance for the class.
    database : Database
        The specific database instance that mongoDBClients connects to.

    Methods:
    -----------
    __init__(database_name: str) -> None
        Intializes the MongoDB connection using given database name.
    """

    client = None   # Shared MongoDB instance across all MongoDB client instances

    def __init__(self,database_name: str = DATABASE_NAME) -> None :
        """
        Intializes the connection to the mongoDB database. If no existing connection is found, it establish new one.

        parameters:
        ------------
        database_name : str , optional
            Name of the mongoDB database to connect to. Default is set by DATABASE_NAME constant.

        Raises:
        -----------
        MyException
            If there is issue connecting to mongoDB or if the environment varible for the mongoDB URL is not set.
        """
        try :
            # check if a mongoDB client connection has already been established ; if not create new one
            if MongoDBClient.client is None :
                mongo_db_url = os.getenv(MONGODB_URL_KEY)    # retrive the mongoDB url from environment variable
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")

                # establish a new MongoDB client connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)

                # used the shared MongoDBClient for this instance 
                self.client = MongoDBClient.client
                self.database = self.client[database_name]  # connect to the specific database
                self.database_name = database_name
                logging.info("MongoDB connection successful.")

        except Exception as e :
            # Raise a custom exception with trackback details if connection fails
            raise MyException(e,sys)