from pymongo.mongo_client import MongoClient

#CONEXIÓN
def conexion():
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): # Se crea la función para leer los datos de MongoDb
    client = conexion() # Se realiza conexión con la base de datos MongoDB
    db = client.actividad4.data_real # Se accede a los datos de 'data_real' en la base de datos 'actividad4'
    data_list = [] #Se almacena la base de datos en un lista
    for data_real_bd in db.find():  # Se iteran a través de todos los documentos en la colección 'data_real' de MongoDB
        data_list.append(data_real_bd) # Se garega cada documento a la lista de datos
    return data_list # Se devuelve  n la lista de datos obtenidos de la base de datos

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""