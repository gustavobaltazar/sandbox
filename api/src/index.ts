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
      data: newAnime,
    });
    return res.status(200).json({ animes });
  } catch (error) {
    return res.status(400).json({ message: "Bad request error", error });
  }
});

const createUserScheme = z.object({
  name: z.string(),
  email: z.string().email(),
  age: z.number().min(14),
  password: z.string().min(12),
});

app.post("/user", async (req, res) => {
  try {
    const { age, name, password, email } = createUserScheme.parse(req.body);
    const passwordHash = password;
    const createdUser = await prisma.user.create({
      data: { name, age, passwordHash, email },
    });
    return res.status(200).json({ user: createdUser });
  } catch (error) {
    return res.status(400).json({ message: "Bad request error", error });
  }
});

const loginScheme = z.object({
  email: z.string().email(),
  password: z.string().min(12),
});

// login (autenticação)
app.post("/user/session", async (req, res) => {
  const { email, password } = loginScheme.parse(req.body);

  const user = await prisma.user.findFirst({
    where: {
      email,
    },
  });

  if (!user) return res.status(404).json({ message: "User not found" });

  const validPassword = password === user.passwordHash;

  if (!validPassword)
    return res.status(400).json({ message: "Invalid password" });

  return res.status(200).json({ user });
});

app.listen(4000, () => {
  console.log("listening on port 4000");
});
