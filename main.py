from pymongo import MongoClient
from datetime import datetime

conn = MongoClient()
db = conn['RegistroOt']


def __getTimeStamp():
    return (datetime.now().strftime('%d.%m.%y %X'))

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
