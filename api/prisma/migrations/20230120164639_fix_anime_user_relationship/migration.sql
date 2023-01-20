/*
  Warnings:

  - You are about to drop the column `userId` on the `Anime` table. All the data in the column will be lost.

*/
-- CreateTable
CREATE TABLE "_AnimeToUser" (
    "A" TEXT NOT NULL,
    "B" TEXT NOT NULL,
    CONSTRAINT "_AnimeToUser_A_fkey" FOREIGN KEY ("A") REFERENCES "Anime" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_AnimeToUser_B_fkey" FOREIGN KEY ("B") REFERENCES "User" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Anime" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "year" TEXT NOT NULL,
    "season" TEXT NOT NULL,
    "genre" TEXT NOT NULL,
    "score" REAL NOT NULL
);
INSERT INTO "new_Anime" ("genre", "id", "name", "score", "season", "year") SELECT "genre", "id", "name", "score", "season", "year" FROM "Anime";
DROP TABLE "Anime";
ALTER TABLE "new_Anime" RENAME TO "Anime";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;

-- CreateIndex
CREATE UNIQUE INDEX "_AnimeToUser_AB_unique" ON "_AnimeToUser"("A", "B");

-- CreateIndex
CREATE INDEX "_AnimeToUser_B_index" ON "_AnimeToUser"("B");
