import pydantic

from uuid import uuid4 as GUID

class Pharmacy(pydantic.BaseModel):
    id: GUID
    name: str
    address: str
    phone_number: int
    latitude: float
    longitude: float
    nocturn: bool


    def makeTableSqlite():
        return """
            CREATE TABLE IF NOT EXISTS pharmacy (
                id CHAR(36) PRIMARY KEY,
                name TEXT,
                address TEXT,
                phone_number INTEGER,
                latitude REAL,
                longitude REAL,
                nocturn INTEGER
            );
        """