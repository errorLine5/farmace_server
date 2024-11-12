import pydantic



class Items(pydantic.BaseModel):

    id: str
    item_name: str
    description_item: str
    id_pharmacy: int
    price: float
    


'''
create table Item(
    id TEXT PRIMARY KEY NOT NULL,
    item_name TEXT NOT NULL,
    description_item TEXT NOT NULL,
    id_pharmacy INTEGER NOT NULL,
    price FLOAT NOT NULL,
    FOREIGN KEY (id_pharmacy) REFERENCES Pharmacy(id) ON DELETE CASCADE ON UPDATE CASCADE
);
'''
