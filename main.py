
from fastapi import FastAPI
from routes.testimonio import testimonio
from database import client

app = FastAPI(title='NER API REST Cuando los pájaros no cantaban', description='Extracción de información \
     de las historias del conflicto armado en Colombia registradas en el Informe de la Comisión de la Verdad. \
     Inicialmente se trata de extracción de personas, lugares y palabras clave de los testimonios en el\
     Libro de las Anticipaciones.', version='0.1')

@app.on_event('startup')
def startup():
    client.server_info

@app.on_event('shutdown')
def shutdown():
    client.close()

app.include_router(testimonio)

def read_document(collection, document_id):
    """Return the contents of the document containing document_id"""
    print("Found a document with _id {}: {}".format(document_id, collection.find_one({"id": document_id})))

@app.get('/')
async def index():
      
    try:
        return "Connection succes"
    except:
        return "Error"
    
    # read_document(collection, document_id)
    