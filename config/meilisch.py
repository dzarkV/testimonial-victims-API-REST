import meilisearch
from dotenv import load_dotenv
from os import getenv

load_dotenv()
urlsch = getenv('URL_MEILISCH')
keysch = getenv('API_KEY_MEILISCH')
indexsch = getenv('INDEX_MEILISCH')

client = meilisearch.Client(urlsch, keysch)
index_search = client.index(indexsch)
