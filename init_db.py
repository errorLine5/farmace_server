import os
from Models.Users import Users
from Models.Pharmacy import Pharmacy
from Models.Worker import Worker
from Services.Database.dbsqlite import DBSqlite
from faker import Faker
import json
import uuid
from datetime import datetime, timedelta
import random
import math



sql_file = open("template_sqlite.sql", "r")
database_file = "database.db"


#delete database
if os.path.exists(database_file):
 os.remove(database_file)
db = DBSqlite(database_file)


commands = sql_file.read().split(";")
for command in commands:
 db.executeRAW(command)


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
            "token_expiration": (datetime.now() + timedelta(days=random.randint(1, 30))).isoformat() if random.random() > 0.5 else None,
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
    # Calculate items per pharmacy (rounded up)
    items_per_pharmacy = math.ceil(num_records / len(pharmacies))
    
    for pharmacy in pharmacies:
        # Generate items for this pharmacy
        for _ in range(items_per_pharmacy):
            item = {
                "id": str(uuid.uuid4()),
                "item_name": fake.catch_phrase(),
                "description_item": fake.text(max_nb_chars=200),
                "id_pharmacy": pharmacy["id"],
                "price": round(random.uniform(1.0, 999.99), 2)
            }
            items.append(item)
            
    # If we generated too many items, trim the list
    return items[:num_records]

# Generate Reservations data
def generate_reservations(users, num_records=25):
    reservations = []
    used_users = set()
    used_dates = set()
    
    for _ in range(min(num_records, len(users))):
        while True:
            user = random.choice(users)
            date = datetime.now() + timedelta(days=random.randint(1, 30))
            if user["id"] not in used_users and date not in used_dates:
                break
                
        reservation = {
            "id": str(uuid.uuid4()),
            "id_user": user["id"],
            "date_reservation": date.isoformat(),
            "dated_price": round(random.uniform(10.0, 500.0), 2)
        }
        reservations.append(reservation)
        used_users.add(user["id"])
        used_dates.add(date)
    return reservations

# Generate List_Item_Reservation data
def generate_list_items_reservations(reservations, items):
    list_items = []
    used_reservations = set()
    used_items = set()
    
    for reservation in reservations:
        while True:
            item = random.choice(items)
            if item["id"] not in used_items:
                break
                
        list_item = {
            "id": str(uuid.uuid4()),
            "id_reservation": reservation["id"],
            "quantity": random.randint(1, 10),
            "id_item": item["id"]
        }
        list_items.append(list_item)
        used_reservations.add(reservation["id"])
        used_items.add(item["id"])
    return list_items

# Generate and insert data
pharmacies = generate_pharmacies()
users = generate_users()
workers = generate_workers(pharmacies, users)
items = generate_items(pharmacies)
reservations = generate_reservations(users)
list_items_reservations = generate_list_items_reservations(reservations, items)

# Insert data into database
for pharmacy in pharmacies:
    db.execute(
        "INSERT INTO Pharmacy (id, nome_farmacia, indirizzo, lat, lng, orari, turni, numeri, sito_web, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (pharmacy["id"], pharmacy["nome_farmacia"], pharmacy["indirizzo"], pharmacy["lat"], pharmacy["lng"], 
         pharmacy["orari"], pharmacy["turni"], pharmacy["numeri"], pharmacy["sito_web"], pharmacy["image"])
    )

for user in users:
    db.execute(
        "INSERT INTO Users (id, password, email, username, first_name, last_name, phone_number, picture, verified, token, token_expiration, can_own, email_token) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (user["id"], user["password"], user["email"], user["username"], user["first_name"], user["last_name"],
         user["phone_number"], user["picture"], user["verified"], user["token"], user["token_expiration"], 
         user["can_own"], user["email_token"])
    )

for worker in workers:
    db.execute(
        "INSERT INTO Worker (id, id_pharmacy, id_user, permission) VALUES (?, ?, ?, ?)",
        (worker["id"], worker["id_pharmacy"], worker["id_user"], worker["permission"])
    )

for item in items:
    db.execute(
        "INSERT INTO Item (id, item_name, description_item, id_pharmacy, price) VALUES (?, ?, ?, ?, ?)",
        (item["id"], item["item_name"], item["description_item"], item["id_pharmacy"], item["price"])
    )

for reservation in reservations:
    db.execute(
        "INSERT INTO Reservation (id, id_user, date_reservation, dated_price) VALUES (?, ?, ?, ?)",
        (reservation["id"], reservation["id_user"], reservation["date_reservation"], reservation["dated_price"])
    )

for list_item in list_items_reservations:
    db.execute(
        "INSERT INTO List_Item_Reservation (id, id_reservation, quantity, id_item) VALUES (?, ?, ?, ?)",
        (list_item["id"], list_item["id_reservation"], list_item["quantity"], list_item["id_item"])
    )

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

db.execute(
    "INSERT INTO Users (id, password, email, username, first_name, last_name, phone_number, picture, verified, token, token_expiration, can_own, email_token) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (default_user["id"], default_user["password"], default_user["email"], default_user["username"], 
     default_user["first_name"], default_user["last_name"], default_user["phone_number"], default_user["picture"], 
     default_user["verified"], default_user["token"], default_user["token_expiration"], default_user["can_own"], 
     default_user["email_token"])
)

print("Database populated successfully!")
print("Default debug user created:")
print("Email: user@mail.com")
print("Password: useUser1")




 


# db.executeRAW(Users.makeTableSqlite())
# db.executeRAW(Pharmacy.makeTableSqlite())