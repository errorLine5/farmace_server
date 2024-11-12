create table Pharmacy(
    id TEXT PRIMARY KEY NOT NULL,
    nome_farmacia TEXT NOT NULL,
    indirizzo TEXT NOT NULL UNIQUE,
    lat FLOAT NOT NULL UNIQUE,
    lng FLOAT NOT NULL UNIQUE,
    orari JSON NOT NULL,
    turni JSON NOT NULL,
    numeri TEXT NOT NULL UNIQUE,
    sito_web TEXT NOT NULL UNIQUE,
    image TEXT
);
create table Users(
    id TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    picture TEXT NOT NULL UNIQUE,
    verified BOOLEAN NOT NULL DEFAULT FALSE,
    token TEXT UNIQUE,
    token_expiration TIMESTAMPTZ,
    can_own BOOLEAN DEFAULT FALSE,
    email_token TEXT UNIQUE
);
create table Worker(
    id TEXT PRIMARY KEY NOT NULL,
    id_pharmacy TEXT NOT NULL UNIQUE,
    id_user TEXT NOT NULL UNIQUE,
    permission INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (id_pharmacy) REFERENCES Pharmacy(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_user) REFERENCES Users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table Reservation(
    id TEXT PRIMARY KEY NOT NULL,
    id_user TEXT NOT NULL UNIQUE,
    date_reservation TIMESTAMPTZ NOT NULL UNIQUE,
    dated_price FLOAT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES Users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table Item(
    id TEXT PRIMARY KEY NOT NULL,
    item_name TEXT NOT NULL UNIQUE,
    description_item TEXT NOT NULL,
    id_pharmacy TEXT NOT NULL,
    price FLOAT NOT NULL,
    FOREIGN KEY (id_pharmacy) REFERENCES Pharmacy(id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table List_Item_Reservation(
    id TEXT PRIMARY KEY NOT NULL,
    id_reservation TEXT NOT NULL UNIQUE,
    quantity INTEGER NOT NULL,
    id_item TEXT NOT NULL UNIQUE,
    FOREIGN KEY (id_reservation) REFERENCES Reservation(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_item) REFERENCES Item(id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    pharmacy_id INTEGER NOT NULL,
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacy (id)
);