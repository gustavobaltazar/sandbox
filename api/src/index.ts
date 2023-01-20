import express from "express";
import cors from "cors";
import { z } from "zod";
import crypto from "crypto";
import { prisma } from "./utils/prisma";

const app = express();

app.use(cors());
app.use(express.json());

const animeScheme = z.object({
  name: z.string(),
  year: z.string(),
  season: z.string(),
  genre: z.string(),
  score: z.number(),
});

app.get("/", (req, res) => {
  return res.status(200).json({ message: "Hello World!" });
});

app.get("/anime", async (req, res) => {
  const allAnimes = await prisma.anime.findMany();
  return res.status(200).json({ animes: allAnimes });
});

app.post("/anime", async (req, res) => {
  try {
    const { name, year, season, genre, score } = animeScheme.parse(req.body);
    const newAnime = { name, year, season, genre, score };
    const animes = await prisma.anime.create({
      data: newAnime
    })
    return res.status(200).json({ animes });
  } catch (error) {
    return res.status(400).json({ message: "Bad request error", error });
  }
});

app.listen(4000, () => {
  console.log("listening on port 4000");
});
