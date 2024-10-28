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
    sito_web TEXT NOT NULL
);'''