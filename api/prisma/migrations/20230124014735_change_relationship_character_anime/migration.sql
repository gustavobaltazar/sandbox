/*
  Warnings:

  - You are about to drop the column `animeId` on the `Character` table. All the data in the column will be lost.

*/
-- CreateTable
CREATE TABLE "_AnimeToCharacter" (
    "A" TEXT NOT NULL,
    "B" TEXT NOT NULL,
    CONSTRAINT "_AnimeToCharacter_A_fkey" FOREIGN KEY ("A") REFERENCES "Anime" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_AnimeToCharacter_B_fkey" FOREIGN KEY ("B") REFERENCES "Character" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Character" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL
);
INSERT INTO "new_Character" ("id", "name") SELECT "id", "name" FROM "Character";
DROP TABLE "Character";
ALTER TABLE "new_Character" RENAME TO "Character";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;

-- CreateIndex
CREATE UNIQUE INDEX "_AnimeToCharacter_AB_unique" ON "_AnimeToCharacter"("A", "B");

-- CreateIndex
CREATE INDEX "_AnimeToCharacter_B_index" ON "_AnimeToCharacter"("B");
