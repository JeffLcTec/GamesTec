import json
import requests
#import firebase_admin
#from firebase_admin import credentials, db


# Inicializa Firebase con tu archivo de credenciales
#if not firebase_admin._apps:
#    cred = credentials.Certificate("arqui-a68cb-firebase-adminsdk-wvdaf-5b49548963.json")
 #   firebase_admin.initialize_app(cred, {
  #      'databaseURL': 'https://arqui-a68cb-default-rtdb.firebaseio.com/'
   # })

with open("juegosjson.json", 'r') as archivo:
     juegos = json.load(archivo)

 ref = db.reference("Lista de juegos")
 ref.set(juegos)

ref = db.reference("Juegos Actualizados")
datos = ref.get()

with open("JuegosActualizado.json", 'w') as archivo:
    json.dump(datos, archivo, indent=4)
