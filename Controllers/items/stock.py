from Services.Auth import Auth
from Services.Sanification import sanitize
from prisma import Prisma

class stock_ctl:
    def __init__(self, dbService):
        self.dbService = dbService
        self.auth = Auth(dbService)

    async def create_stock(self, id, id_item, quantity, price, email, token):
        id = sanitize(id)
        id_item = sanitize(id_item)
        quantity = sanitize(quantity)
        price = sanitize(price)

        prisma = Prisma()
        await prisma.connect()

    
        self.auth.isAuth(email=email, token=token)

        stock = await prisma.stock.create(
            id = id,
            id_item = id_item,
            quantity = quantity,
            price = price)
        
        print(stock)
        await prisma.disconnect()
        return {"status": "success", "operation": "create", "id_stock": id}
    
    async def get_stock(self, id, email, token):
        id = sanitize(id)
        email = sanitize(email)
        token = sanitize(token)

        self.auth.isAuth(email=email, token=token)

        prisma = Prisma()
        await prisma.connect()

        # Get all stocks for the pharmacy
        stocks = await prisma.stock.find_many(
            where = {
                "id_pharmacy": id
            },
            include = {
                "item": True  # Include the related item data
            }
        )

        # Format the response
        formatted_stocks = []
        for stock in stocks:
            formatted_stocks.append({
                "id": stock.id,
                "id_item": stock.id_item,
                "quantity": stock.quantity,
                "price": stock.price,
                "id_pharmacy": stock.id_pharmacy,
                "item": {
                    "id": stock.item.id,
                    "item_name": stock.item.item_name,
                    "description_item": stock.item.description_item,
                    "price": stock.item.price,
                    "category": stock.item.category,
                    "image": stock.item.image,
                    "id_pharmacy": stock.item.id_pharmacy
                } if stock.item else None
            })

        await prisma.disconnect()
        return {"status": "success", "operation": "get", "stock": formatted_stocks}
    
    async def modify_stock(self, id, id_item, quantity, price, email, token):
        id = sanitize(id)
        id_item = sanitize(id_item)
        quantity = sanitize(quantity)
        price = sanitize(price)

        self.auth.isAuth(email=email, token=token)
        
        prisma = Prisma()
        await prisma.connect()

        stock = await prisma.stock.update(
            where = {
                "id": id
            },
            data = {
                "quantity": quantity,
                "price": price}
        )
        await prisma.disconnect()
        return {"status": "success", "operation": "modify", "stock": stock}
    
    async def delete_stock(self, id, email, token):
        id = sanitize(id)
        email = sanitize(email)
        token = sanitize(token)
        
        self.auth.isAuth(email=email, token=token)

        prisma = Prisma()
        await prisma.connect()

        stock = await prisma.stock.delete(
            where = {
                "id": id
            }
        )
        await prisma.disconnect()
        return {"status": "success", "operation": "delete", "stock": stock}