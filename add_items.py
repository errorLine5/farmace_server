import asyncio
from prisma import Prisma
import uuid

async def add_items():
    prisma = Prisma()
    await prisma.connect()

    # First, get a pharmacy ID
    pharmacy = await prisma.pharmacy.find_first()
    if not pharmacy:
        print("No pharmacy found in the database. Please run init_db.py first.")
        await prisma.disconnect()
        return

    items = [
        {
            "nome": "Crema mani Nivea",
            "prezzo": 10.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Cosmesi",
        },
        {
            "nome": "Tachipirina 500mg",
            "prezzo": 5.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Mal di testa",
        },
        {
            "nome": "Paracetamolo 500mg",
            "prezzo": 3.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Mal di pancia",
        },
        {
            "nome": "Bissolvon 100mg",
            "prezzo": 10.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Mal di gola",
        },
        {
            "nome": "Bissolvon Lintus 100mg",
            "prezzo": 10.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Mal di gola",
        },
        {
            "nome": "Cerotti",
            "prezzo": 3.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Medicazioni",
        },
        {
            "nome": "Caramelle Gola",
            "prezzo": 1.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Mal di gola",
        },
        {
            "nome": "Bende 100x100mm",
            "prezzo": 1.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Medicazioni",
        },
        {
            "nome": "Cerave",
            "prezzo": 20.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Cosmesi",
        },
        {
            "nome": "Shampoo per i capelli",
            "prezzo": 20.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Cosmesi",
        },
        {
            "nome": "Spazzolino elettrico OralB",
            "prezzo": 200.0,
            "immagine": "https://picsum.photos/200/300",
            "categoria": "Elettronica",
        },
    ]

    for item in items:
        # Create the item
        new_item = await prisma.item.create(
            data={
                "id": str(uuid.uuid4()),
                "item_name": item["nome"],
                "description_item": f"Description for {item['nome']}",
                "price": item["prezzo"],
                "category": item["categoria"],
                "image": item["immagine"],
                "id_pharmacy": pharmacy.id
            }
        )

        # Create stock for the item
        await prisma.stock.create(
            data={
                "id": str(uuid.uuid4()),
                "id_item": new_item.id,
                "quantity": 100,  # Default quantity
                "price": item["prezzo"],
                "id_pharmacy": pharmacy.id
            }
        )

        print(f"Added item: {item['nome']}")

    await prisma.disconnect()
    print("All items added successfully!")

if __name__ == "__main__":
    asyncio.run(add_items()) 