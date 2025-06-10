-- CreateTable
CREATE TABLE "Pharmacy" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "nome_farmacia" TEXT NOT NULL,
    "indirizzo" TEXT NOT NULL,
    "lat" REAL NOT NULL,
    "lng" REAL NOT NULL,
    "orari" TEXT NOT NULL,
    "turni" TEXT NOT NULL,
    "numeri" TEXT NOT NULL,
    "sito_web" TEXT NOT NULL,
    "image" TEXT
);

-- CreateTable
CREATE TABLE "Item" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "item_name" TEXT NOT NULL,
    "description_item" TEXT NOT NULL,
    "price" REAL NOT NULL,
    "id_pharmacy" TEXT NOT NULL,
    CONSTRAINT "Item_id_pharmacy_fkey" FOREIGN KEY ("id_pharmacy") REFERENCES "Pharmacy" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "phone_number" TEXT NOT NULL,
    "picture" TEXT NOT NULL,
    "verified" BOOLEAN NOT NULL DEFAULT false,
    "token" TEXT,
    "token_expiration" DATETIME,
    "can_own" BOOLEAN NOT NULL DEFAULT false,
    "email_token" TEXT
);

-- CreateTable
CREATE TABLE "Worker" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "permission" INTEGER NOT NULL,
    "id_pharmacy" TEXT NOT NULL,
    "id_user" TEXT NOT NULL,
    CONSTRAINT "Worker_id_pharmacy_fkey" FOREIGN KEY ("id_pharmacy") REFERENCES "Pharmacy" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "Worker_id_user_fkey" FOREIGN KEY ("id_user") REFERENCES "User" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "User_username_key" ON "User"("username");
