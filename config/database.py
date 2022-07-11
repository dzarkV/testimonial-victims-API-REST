import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

conn = pymongo.MongoClient(config['MONGO_CONNECTION_STRING'])
# cliente.server_info() # validate connection string
# db = cliente[config['DB_NAME']]
# collection = db.get_collection(config['COLLECTION_NAME'])

