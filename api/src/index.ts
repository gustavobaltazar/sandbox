import express, { NextFunction, Request, Response } from "express";
import cors from "cors";
import { z } from "zod";
import crypto from "crypto";
import { prisma } from "./utils/prisma";
import { isAuthenticated, isAuthenticatedRequest } from "./utils/middleware";

const app = express();

app.use(cors());
app.use(express.json());

const animeScheme = z.object({
  name: z.string(),
  year: z.string(),
  season: z.string(),
  genre: z.string(),
  score: z.number(),
  synopsis: z.string().max(500),
});

app.get("/", (req, res) => {
  return res.status(200).json({ message: "Hello World!" });
});

app.get("/anime", async (req, res) => {
  const allAnimes = await prisma.anime.findMany({
    include: {
      Character: true,
    },
  });
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

app.post("/anime/character", async (req, res) => {
  function isCreateCharacter(
    characterInput: Zimbas
  ): characterInput is CreateCharacter {
    return "characterName" in characterInput;
  }
  const characterInput = addAnimeCharacterScheme.parse(req.body);
  try {
    let anime;
    if (isCreateCharacter(characterInput)) {
      anime = await prisma.anime.update({
        where: {
          id: characterInput.animeId,
        },
        data: {
          Character: {
            create: {
              name: characterInput.characterName,
            },
          },
        },
        include: {
          Character: true,
        },
      });
    } else {
      anime = await prisma.anime.update({
        where: {
          id: characterInput.animeId,
        },
        data: {
          Character: {
            connect: {
              id: characterInput.characterId,
            },
          },
        },
        include: {
          Character: true,
        },
      });
    }
    return res.status(200).json({ anime });
  } catch (error) {
    return res.status(400).json({ message: "Cannot add character!", error });
  }
});

app.get("/anime/character", async (req, res) => {
  const allCharacter = await prisma.character.findMany({
    include: {
      animes: true
    }
  })
  return res.status(200).json({ allCharacter })
})

const addAnimeFavoriteScheme = z.object({
  animeId: z.string(),
});

const addAnimeCharacterScheme = z
  .object({
    characterId: z.string(),
    animeId: z.string(),
  })
  .or(
    z.object({
      characterName: z.string(),
      animeId: z.string(),
    })
  );
type Zimbas = z.infer<typeof addAnimeCharacterScheme>;
type CreateCharacter = {
  characterName: string;
  animeId: string;
};

app.post(
  "/user/favorite/anime",
  isAuthenticated,
  async (req: isAuthenticatedRequest, res) => {
    const { animeId } = addAnimeFavoriteScheme.parse(req.body);

    try {
      const user = await prisma.user.update({
        where: {
          id: req.user?.id,
        },
        data: {
          favoriteAnimes: {
            connect: {
              id: animeId,
            },
          },
        },
        include: {
          favoriteAnimes: true,
        },
      });

      return res.status(200).json({ user });
    } catch (error) {
      return res
        .status(400)
        .json({ message: "Cannot add anime to user favorite list" });
    }
  }
);

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

app.post(
  "/user/me",
  isAuthenticated,
  async (req: isAuthenticatedRequest, res) => {
    return res.status(200).json({ user: req.user });
  }
);

app.listen(4000, () => {
  console.log("listening on port 4000");
});
