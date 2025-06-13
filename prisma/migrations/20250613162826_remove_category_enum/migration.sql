-- CreateTable
CREATE TABLE "Stock" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "id_item" TEXT NOT NULL,
    "quantity" INTEGER NOT NULL,
    "price" REAL NOT NULL,
    "id_pharmacy" TEXT NOT NULL,
    CONSTRAINT "Stock_id_pharmacy_fkey" FOREIGN KEY ("id_pharmacy") REFERENCES "Pharmacy" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- RedefineTables
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Item" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "item_name" TEXT NOT NULL,
    "description_item" TEXT NOT NULL,
    "price" REAL NOT NULL,
    "category" TEXT NOT NULL DEFAULT 'OTHER',
    "image" TEXT,
    "id_pharmacy" TEXT NOT NULL,
    CONSTRAINT "Item_id_pharmacy_fkey" FOREIGN KEY ("id_pharmacy") REFERENCES "Pharmacy" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO "new_Item" ("description_item", "id", "id_pharmacy", "item_name", "price") SELECT "description_item", "id", "id_pharmacy", "item_name", "price" FROM "Item";
DROP TABLE "Item";
ALTER TABLE "new_Item" RENAME TO "Item";
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;
