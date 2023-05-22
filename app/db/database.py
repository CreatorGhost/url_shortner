import motor.motor_asyncio
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import DB_PASSWORD

# create an instance of MongoClient
client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb+srv://testing_db:{DB_PASSWORD}@urlshortener.qrk6fdg.mongodb.net/?retryWrites=true&w=majority')

# create an instance of the database
database = client['urls_db']





# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://testing_db:<password>@urlshortener.qrk6fdg.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)