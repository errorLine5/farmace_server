import pydantic

class Worker(pydantic.BaseModel):
 id: str
 id_pharmacy: str
 id_user: str
 permission: int
 
 