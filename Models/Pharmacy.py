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

   