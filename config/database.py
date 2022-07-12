import pymongo
from dotenv import dotenv_values, find_dotenv

path = find_dotenv()
config = dotenv_values(dotenv_path=path)

conn = pymongo.MongoClient(config['MONGO_CONNECTION_STRING'])
# cliente.server_info() # validate connection string
db = conn[config['DB_NAME']]
collection = db.get_collection(config['COLLECTION_NAME'])

