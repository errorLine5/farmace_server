from Models.Pharmacy import Pharmacy
from Services.Auth import Auth
import fastapi
from tools.funzioni_di_ricerca import haversine_formula, pharmacy_in_range
from prisma import Prisma


class ricerca_ctl():

    def __init__(self, dbservice):
        self.dbService = dbservice
        self.auth = Auth(dbservice)

    async def ricerca(self, user_lat, user_lng, range)->list[Pharmacy]:
        prisma = Prisma()
        await prisma.connect()
        pharmacies = await prisma.pharmacy.find_many(

            where={
                "lat": {
                    "lte": user_lat + range,
                    "gte": user_lat - range
                },
                "lng": {
                    "lte": user_lng + range,
                    "gte": user_lng - range
                }
            }
        )
        keys  =pharmacies[0].model_dump().keys()
        print("keys:\n", keys, len(keys))

        pharmacyList= [pharmacy.model_dump() for pharmacy in pharmacies]
        await prisma.disconnect()
        return pharmacyList