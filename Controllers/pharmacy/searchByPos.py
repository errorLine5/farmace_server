from Models.Pharmacy import Pharmacy
from Models.Pharmacy import Coordinates_Range
from Services.Sanification import sanitize
from Services.FieldValidation import FieldValidation
from Services.Auth import Auth
from tools.Query import BuildQuery
import fastapi  


class SearchByPos_pharmacy_ctl:

    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)


    def search_by_pos(self, minLat: float, maxLat: float, minLng: float, maxLng: float, email, token)->list[Pharmacy]:
        
        self.auth.isAuth(email=email, token=token)

        query='''
        SELECT id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web
        FROM Pharmacy
        WHERE lat BETWEEN ? AND ?
        AND lng BETWEEN ? AND ?
        '''

        result=self.dbService.execute(query, (minLat, maxLat, minLng, maxLng))

        rows=result.fetchall()
        pharmacies=[Pharmacy(id=row[0], nome_farmacia=row[1], indirizzo=row[2], lat=row[3], lng=row[4], orari=row[5], turni=row[6], numeri=row[7], sito_web=row[8]) for row in rows]
        if len(pharmacies)==0:
            raise fastapi.HTTPException(status_code=404, detail="No pharmacy found")
        else:
            return pharmacies


        