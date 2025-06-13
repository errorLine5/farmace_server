import os
from prisma import Prisma
from faker import Faker
import json
import uuid
from datetime import datetime, timedelta
import random
import math

# Initialize Prisma client
prisma = Prisma()

# Initialize Faker
fake = Faker()

# Generate Pharmacy data
def generate_pharmacies(num_records=10):
    pharmacies = []
    for _ in range(num_records):
        working_hours = {
            "monday": f"{random.randint(8,10)}:00-{random.randint(17,20)}:00",
            "tuesday": f"{random.randint(8,10)}:00-{random.randint(17,20)}:00",
            "wednesday": f"{random.randint(8,10)}:00-{random.randint(17,20)}:00",
            "thursday": f"{random.randint(8,10)}:00-{random.randint(17,20)}:00",
            "friday": f"{random.randint(8,10)}:00-{random.randint(17,20)}:00",
            "saturday": f"{random.randint(8,10)}:00-{random.randint(13,15)}:00",
            "sunday": "closed"
        }
        
        shifts = {
            "2024": {
                "january": [1, 15, 30],
                "february": [14, 28]
            }
        }
        
        pharmacy = {
            "id": str(uuid.uuid4()),
            "nome_farmacia": f"Farmacia {fake.company()}",
            "indirizzo": fake.address().replace("\n", ", "),
            "lat": float(fake.latitude()),
            "lng": float(fake.longitude()),
            "orari": json.dumps(working_hours),
            "turni": json.dumps(shifts),
            "numeri": fake.phone_number(),
            "sito_web": fake.url(),
            "image": f"https://picsum.photos/id/{random.randint(1, 1000)}/900/900"
        }
        pharmacies.append(pharmacy)
    return pharmacies

# Generate Users data
def generate_users(num_records=20):
    users = []
    for _ in range(num_records):
        user = {
            "id": str(uuid.uuid4()),
            "password": fake.password(),
            "email": fake.email(),
            "username": fake.user_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "picture": f"https://picsum.photos/id/{random.randint(1, 1000)}/200/300",
            "verified": random.choice([True, False]),
            "token": str(uuid.uuid4()) if random.random() > 0.5 else None,
            "token_expiration": (datetime.now() + timedelta(days=random.randint(1, 30))) if random.random() > 0.5 else None,
            "can_own": random.choice([True, False]),
            "email_token": str(uuid.uuid4()) if random.random() > 0.5 else None
        }
        users.append(user)
    return users

# Generate Worker data
def generate_workers(pharmacies, users, num_records=15):
    workers = []
    used_pharmacies = set()
    used_users = set()
    
    for _ in range(min(num_records, len(pharmacies), len(users))):
        while True:
            pharmacy = random.choice(pharmacies)
            user = random.choice(users)
            if pharmacy["id"] not in used_pharmacies and user["id"] not in used_users:
                break
        
        worker = {
            "id": str(uuid.uuid4()),
            "id_pharmacy": pharmacy["id"],
            "id_user": user["id"],
            "permission": random.randint(0, 3)
        }
        workers.append(worker)
        used_pharmacies.add(pharmacy["id"])
        used_users.add(user["id"])
    return workers

# Generate Items data
def generate_items(pharmacies, num_records=30):
    items = []
    items_per_pharmacy = math.ceil(num_records / len(pharmacies))
    
    for pharmacy in pharmacies:
        for _ in range(items_per_pharmacy):
            item = {
                "id": str(uuid.uuid4()),
                "item_name": fake.catch_phrase(),
                "description_item": fake.text(max_nb_chars=200),
                "id_pharmacy": pharmacy["id"],
                "price": round(random.uniform(1.0, 999.99), 2),
                "category": random.choice(["DRUGS", "COSMETICS", "BABY", "FOOD", "PETS", "TOOLS", "HOME", "CLOTHING", "ELECTRONICS", "SPORTS", "OTHER"]),
                "image": f"https://picsum.photos/id/{random.randint(1, 1000)}/900/900",
                "quantity": random.randint(1, 100)
            
            }
            items.append(item)
            
    return items[:num_records]

async def main():
    # Connect to the database
    await prisma.connect()

    # Generate data
    pharmacies = generate_pharmacies()
    users = generate_users()
    workers = generate_workers(pharmacies, users)
    items = generate_items(pharmacies)

    # Insert data into database
    for pharmacy in pharmacies:
        await prisma.pharmacy.create(data=pharmacy)

    for user in users:
        await prisma.user.create(data=user)

    for worker in workers:
        await prisma.worker.create(data=worker)

    for item in items:
        await prisma.item.create(data=item)

    # Add default debug user
    default_user = {
        "id": str(uuid.uuid4()),
        "password": "useUser1.",
        "email": "user@mail.com",
        "username": "debuguser",
        "first_name": "Debug",
        "last_name": "User",
        "phone_number": "+1234567890",
        "picture": "https://picsum.photos/id/1/200/300",
        "verified": True,
        "token": None,
        "token_expiration": None,
        "can_own": True,
        "email_token": None
    }

    await prisma.user.create(data=default_user)

    print("Database populated successfully!")
    print("Default debug user created:")
    print("Email: user@mail.com")
    print("Password: useUser1")

    # Disconnect from the database
    await prisma.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())