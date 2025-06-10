/*
  Warnings:

  - You are about to drop the column `token` on the `User` table. All the data in the column will be lost.
  - You are about to drop the column `token_expiration` on the `User` table. All the data in the column will be lost.

*/
-- RedefineTables
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_User" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "phone_number" TEXT NOT NULL,
    "picture" TEXT NOT NULL,
    "verified" BOOLEAN NOT NULL DEFAULT false,
    "can_own" BOOLEAN NOT NULL DEFAULT false,
    "email_token" TEXT
);
INSERT INTO "new_User" ("can_own", "email", "email_token", "first_name", "id", "last_name", "password", "phone_number", "picture", "username", "verified") SELECT "can_own", "email", "email_token", "first_name", "id", "last_name", "password", "phone_number", "picture", "username", "verified" FROM "User";
DROP TABLE "User";
ALTER TABLE "new_User" RENAME TO "User";
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");
CREATE UNIQUE INDEX "User_username_key" ON "User"("username");
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;
