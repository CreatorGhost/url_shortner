import motor.motor_asyncio
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from config import DB_PASSWORD


# create an instance of MongoClient
client = motor.motor_asyncio.AsyncIOMotorClient(
    f"mongodb+srv://testing_db:{DB_PASSWORD}@urlshortener.qrk6fdg.mongodb.net/?retryWrites=true&w=majority"
)

database = client.urls_db


try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
