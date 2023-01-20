import express from "express";
import cors from "cors";
import { z } from "zod";
import crypto from "crypto";
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


type Anime = z.infer<typeof animeScheme> & { id: string };

let animes: Anime[] = [];

app.get("/", (req, res) => {
  return res.status(200).json({ message: "Hello World!" });
});

app.get("/anime", (req, res) => {
  return res.status(200).json({ animes });
});

app.post("/anime", (req, res) => {
  try {
    const { name, year, season, genre, score } = animeScheme.parse(req.body);
    const id = crypto.randomUUID();
    const newAnime = { id, name, year, season, genre, score };
    animes.push(newAnime);
    return res.status(200).json({ animes });
  } catch (error) {
    return res.status(400).json({ message: "Bad request error", error });
  }
});

app.listen(4000, () => {
  console.log("listening on port 4000");
});
