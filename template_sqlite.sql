create table Pharmacy(
    id TEXT PRIMARY KEY NOT NULL,
    nome_farmacia TEXT NOT NULL,
    indirizzo TEXT NOT NULL,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    orari JSON NOT NULL,
    turni JSON NOT NULL,
    numeri TEXT NOT NULL,
    sito_web TEXT NOT NULL
);
create table Users(
    id TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    picture TEXT NOT NULL,
    verified BOOLEAN NOT NULL DEFAULT FALSE,
    token TEXT,
    token_expiration DATETIME,
    can_own BOOLEAN DEFAULT FALSE,
    email_token TEXT
);
-- permission = 0 -> default_worker : permission to edit items and reservation
-- permission = 1 -> manager : permition to edit workers and items
-- permission = 2 -> admin : permition to edit workers, items and pharmacy
create table Worker(
    id TEXT PRIMARY KEY NOT NULL,
    id_pharmacy TEXT NOT NULL,
    id_user TEXT NOT NULL,
    UNIQUE (id_user),
    permission INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (id_pharmacy) REFERENCES Pharmacy(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_user) REFERENCES Users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table Reservation(
    id TEXT PRIMARY KEY NOT NULL,
    id_user INTEGER NOT NULL,
    date_r DATETIME NOT NULL,
    dated_price FLOAT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES Users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table Item(
    id TEXT PRIMARY KEY NOT NULL,
    item_name TEXT NOT NULL,
    description_item TEXT NOT NULL,
    id_pharmacy INTEGER NOT NULL,
    price FLOAT NOT NULL,
    FOREIGN KEY (id_pharmacy) REFERENCES Pharmacy(id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table List_Item_Reservation(
    id TEXT PRIMARY KEY NOT NULL,
    id_res INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    id_item INTEGER NOT NULL,
    FOREIGN KEY (id_res) REFERENCES Reservation(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_item) REFERENCES Item(id) ON DELETE CASCADE ON UPDATE CASCADE
);