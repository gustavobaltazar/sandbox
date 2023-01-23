import express, { NextFunction, Request, Response } from "express";
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
    const newAnime = animeScheme.parse(req.body);
    const animes = await prisma.anime.create({
      data: newAnime,
    });
    return res.status(200).json({ animes });
  } catch (error) {
    return res.status(400).json({ message: "Bad request error", error });
  }
});

const addAnimeFavorite = z.object({
  animeId: z.string()
})

const isAuthenticatedScheme = z.object({
  sessionId: z.string(),
})

const isAuthenticated = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { sessionId } = isAuthenticatedScheme.parse(req.body);
    const session = await prisma.session.findUnique({
      where: {
        sessionId,
      },
    });
  
    if (!session) return res.status(404).json({ message: "Session not found" });
  
    const user = await prisma.user.findUnique({
      where: {
        id: session.userId,
      },
    });
    if (!user) return res.status(404).json({ message: "User not found" });
    req.user = user;
    next()
  } catch (error) {
    return res.status(400).json({ message: "UNATHORIZED" })
  }
};

app.post("/user/favorite/anime", isAuthenticated, async (req, res) => {
  const { animeId } = addAnimeFavorite.parse(req.body);

  try {
    const user = await prisma.user.update({
      where: {
        id: req.user.id
      },
      data: {
        favoriteAnimes: {
          connect: {
            id: animeId
          }
        }
      },
      include: {
        favoriteAnimes: true
      }
    });

    return res.status(200).json({ user });
  } catch (error) {
    return res.status(400).json({ message: "Cannot add anime to user favorite list" }); 
  }
})

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
    return res.status(401).json({ message: "Invalid password" });

  const newSession = await prisma.session.create({
    data: {
      userId: user.id,
    },
  });

  const newSessionId = newSession.sessionId;

  return res.status(200).json({ newSessionId });
});

app.delete("/user/session", async (req, res) => {
  const { sessionId } = z
    .object({
      sessionId: z.string(),
    })
    .parse(req.body);

  try {
    await prisma.session.delete({
      where: {
        sessionId,
      },
    });
    return res.status(200).json({ message: "Logout succesfully" });
  } catch (err) {
    return res.status(500).json({ message: "Something went wrong!" });
  }
});

app.post("/user/me", isAuthenticated, async (req, res) => {
  return res.status(200).json({ user: req.user });
});

app.listen(4000, () => {
  console.log("listening on port 4000");
});
