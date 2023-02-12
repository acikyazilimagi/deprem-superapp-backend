import os
import re

import certifi
import pymongo
from dotenv import find_dotenv, load_dotenv
from fastapi import HTTPException
from loguru import logger
from pymongo import MongoClient

ca = certifi.where()

load_dotenv(find_dotenv())


class DbWrapper:
    def __init__(self):
        self.setup()

    def setup(self) -> bool:
        """
        :return: True if connected to the MongoDB, Error otherwise
        """
        try:
            self.connection_string = os.environ.get("MONGODB_PWD")
            self.client = MongoClient(self.connection_string, tlsCAFile=ca)

            logger.info("Connected to MongoDB. Setup has completed.")

            return True

        except Exception as e:
            logger.error(e)
            return e

    def get_database_names(self):
        """
        :return: a list of all the database names
        """
        try:
            dbs = self.client.list_database_names()

            logger.info("Database names method was called.")

            return dbs

        except Exception as e:
            logger.error(e)
            return e

    def get_database(self, db_name: str):
        """
        :param db_name: the name of the database to get
        :return: the database object
        """
        try:
            db = self.client[db_name]

            logger.info("Database method was called.")

            return db

        except Exception as e:
            logger.error(e)
            return e

    def get_collections_names(self, db_name: str):
        """
        :param db_name: the name of the database to get the collections from
        :return: a list of all the collections in the database
        """
        try:
            db = self.get_database(db_name)
            collections = db.list_collection_names()

            logger.info("Collections names method was called.")

            return collections

        except Exception as e:
            logger.error(e)
            return e

    def get_collection(self, collection_name: str):
        """
        :param collection_name: the name of the collection to get
        :return: the collection object
        """
        try:
            db = self.get_database("deprem")
            collection = db[collection_name]

            logger.info("Collection method was called.")

            return collection

        except Exception as e:
            logger.error(e)
            return e

    def tr_lower(self, string_data):
        string_data = re.sub(r"İ", "i", string_data)
        string_data = re.sub(r"I", "ı", string_data)
        string_data = re.sub(r"Ç", "ç", string_data)
        string_data = re.sub(r"Ş", "ş", string_data)
        string_data = re.sub(r"Ü", "ü", string_data)
        string_data = re.sub(r"Ğ", "ğ", string_data)
        string_data = string_data.lower()  # for the rest use default lower
        return string_data

    def set_map_data(self, payload: dict):
        """
        :param payload: the data to insert
        :return: the inserted data
        """
        try:
            collection = self.get_collection("map_data")

            logger.info("Set map data method was called.")

            if payload["notlar"]:
                payload["notlar"] = self.tr_lower(payload["notlar"])

            return HTTPException(
                status_code=200,
                detail=collection.insert_one(payload).inserted_id,
            )

        except Exception as e:
            logger.error(e)
            return HTTPException(
                status_code=500,
                detail="An error occurred while inserting the data.",
            )

    def set_service_point(self, payload: dict):
        """
        :param payload: the data to insert
        :return: the inserted data
        """
        try:
            collection = self.get_collection("service_points")

            logger.info("Set service point method was called.")

            if payload["notlar"]:
                payload["notlar"] = self.tr_lower(payload["notlar"])

            return HTTPException(
                status_code=200,
                detail=collection.insert_one(payload).inserted_id,
            )

        except Exception as e:
            logger.error(e)
            return HTTPException(
                status_code=500,
                detail="An error occurred while inserting the data.",
            )

    def get_service_point(self, payload: dict):
        """
        :param payload: the data to get
        :return: the data
        """
        try:
            collection = self.get_collection("service_points")

            logger.info("Get service point method was called.")

            query = {}

            if payload["il"]:
                query["il"] = payload["il"]
            if payload["ilce"]:
                query["ilce"] = payload["ilce"]
            if payload["servis"]:
                query["servis"] = {"$all": payload["servis"]}
            if payload["notlar"]:
                query["notlar"] = {"$regex": f".*{self.tr_lower(payload['notlar'])}.*"}

            logger.info(query)

            return HTTPException(status_code=200, detail=list(collection.find(query)))

        except Exception as e:
            logger.error(e)
            return HTTPException(
                status_code=500,
                detail="An error occurred while getting the data.",
            )

    def get_map_data(self, payload: dict):
        """
        :param payload: the data to get
        :return: the data
        """
        try:
            collection = self.get_collection("map_data")

            logger.info("Get map data method was called.")

            query = {}

            if payload["guncel_tarih"]:
                query["zaman"] = {"$gt": payload["guncel_tarih"]}
                return HTTPException(
                    status_code=200, detail=list(collection.find(query))
                )

            else:
                if payload["il"]:
                    query["il"] = payload["il"]
                if payload["ilce"]:
                    query["ilce"] = payload["ilce"]
                if payload["gereksinimler"]:
                    query["gereksinimler"] = {"$all": payload["gereksinimler"]}
                if payload["notlar"]:
                    query["notlar"] = {
                        "$regex": f".*{self.tr_lower(payload['notlar'])}.*"
                    }
                if payload["baslangic_zaman"] and payload["bitis_zaman"]:
                    query["zaman"] = {
                        "$lte": payload["bitis_zaman"],
                        "$gte": payload["baslangic_zaman"],
                    }

                return HTTPException(
                    status_code=200,
                    detail=list(
                        collection.find(query).sort("zaman", pymongo.DESCENDING)
                    ),
                )

        except Exception as e:
            logger.error(e)
            return HTTPException(
                status_code=500,
                detail="An error occurred while getting the data.",
            )

    def test_set_map_data(self, payload: dict):
        """
        :param payload: the data to insert
        :return: the inserted data
        """

        try:
            collection = self.get_collection("test_map_data")

            logger.info("Test Set map data method was called.")

            if payload["notlar"]:
                payload["notlar"] = self.tr_lower(payload["notlar"])

            return HTTPException(
                status_code=200,
                detail=collection.insert_one(payload).inserted_id,
            )

        except Exception as e:
            logger.error(e)
            return HTTPException(
                status_code=500,
                detail="An error occurred while inserting the data.",
            )

    def test_get_map_data(self, payload: dict):
        """
        :param payload: the data to get
        :return: the data
        """
        try:
            collection = self.get_collection("test_map_data")

            logger.info("Test Get map data method was called.")

            query = {}

            if payload["guncel_tarih"]:
                query["zaman"] = {"$gt": payload["guncel_tarih"]}
                return HTTPException(
                    status_code=200, detail=list(collection.find(query))
                )

            else:
                if payload["il"]:
                    query["il"] = payload["il"]
                if payload["ilce"]:
                    query["ilce"] = payload["ilce"]
                if payload["gereksinimler"]:
                    query["gereksinimler"] = {"$all": payload["gereksinimler"]}
                if payload["notlar"]:
                    query["notlar"] = {
                        "$regex": f".*{self.tr_lower(payload['notlar'])}.*"
                    }
                if payload["baslangic_zaman"] and payload["bitis_zaman"]:
                    query["zaman"] = {
                        "$lte": payload["bitis_zaman"],
                        "$gte": payload["baslangic_zaman"],
                    }

                return HTTPException(
                    status_code=200,
                    detail=list(
                        collection.find(query).sort("zaman", pymongo.DESCENDING)
                    ),
                )

        except Exception as e:
            logger.error(e)
            return HTTPException(
                status_code=500,
                detail="An error occurred while getting the data.",
            )
