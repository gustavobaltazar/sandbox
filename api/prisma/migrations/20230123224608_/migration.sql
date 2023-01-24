/*
  Warnings:

  - Added the required column `synopsis` to the `Anime` table without a default value. This is not possible if the table is not empty.

*/
-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Anime" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "year" TEXT NOT NULL,
    "season" TEXT NOT NULL,
    "genre" TEXT NOT NULL,
    "score" REAL NOT NULL,
    "synopsis" TEXT NOT NULL
);
INSERT INTO "new_Anime" ("genre", "id", "name", "score", "season", "year") SELECT "genre", "id", "name", "score", "season", "year" FROM "Anime";
DROP TABLE "Anime";
ALTER TABLE "new_Anime" RENAME TO "Anime";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
