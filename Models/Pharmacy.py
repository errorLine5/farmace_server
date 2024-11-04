import pydantic



class Pharmacy(pydantic.BaseModel):

    id: str
    nome_farmacia: str
    indirizzo: str
    lat: float
    lng: float
    orari: str
    turni: str
    numeri: str
    sito_web: str
    image: str


    
class Coordinates_Range(pydantic.BaseModel):
    
    latitude: float
    longitude: float
    range: float

class date_time(pydantic.BaseModel):
    giorno: str
    orario_corrente: str 

'''
create table Pharmacy(
    id TEXT PRIMARY KEY NOT NULL,
    nome_farmacia TEXT NOT NULL,
    indirizzo TEXT NOT NULL,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    orari JSON NOT NULL,
    turni JSON NOT NULL,
    numeri TEXT NOT NULL,
    sito_web TEXT NOT NULL,
    image TEXT
);'''

#   FORMATO ORARI
#  '''orari_settimanali = [
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Lunedì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Martedì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Mercoledì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Giovedì
#     [ ["09:00", "12:30"], ["15:30", "18:00"]],  # Venerdì
#     [ ["09:00", "13:00"], ["15:30", "18:00"]],   # Sabato
#     [ [None, None], [None, None]]               # Domenica
# ]'''