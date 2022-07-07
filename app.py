import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

def read_document(collection, document_id):
    """Return the contents of the document containing document_id"""
    print("Found a document with _id {}: {}".format(document_id, collection.find_one({"id": document_id})))

def main():
    """Connect to the API for MongoDB, and read a document"""
    cliente = pymongo.MongoClient(config['COSMOS_CONNECTION_STRING'])
    try:
        cliente.server_info() # validate connection string
        db = cliente[config['DB_NAME']]
        collection = db.get_collection(config['COLLECTION_NAME'])
        print("Connection succes! Database and document with id = 1", read_document(collection, 1))
        cliente.close()
    except pymongo.errors.OperationFailure as e:
        raise print("Error", e)
    
    read_document(collection, document_id)
   
if __name__ == '__main__':
    main()