from pymongo import MongoClient
from datetime import datetime

conn = MongoClient()

#creo y conecto a la base de datos
db = conn['RegistroOt']

#funcion de ayuda para obtener fecha y hora actuales.
def __getTimeStamp():
    return (datetime.now().strftime('%d.%m.%y %X'))

#defino los esquemas con los que voy a trabajar
Tecnico = {
    'Nombre':'',
    'Especialidad': ''
}

Ot = {
    'Fecha': '',
    'Tecnico': '',
    'Observaciones':'',
    'NroOt':'',
    'Materiales':[]
}
#------------------------------------------------
