import { Router } from "express";
import { z } from "zod";
import { isAuthenticated, isAuthenticatedRequest } from "../utils/middleware";
import { prisma } from "../utils/prisma";

const router = Router();

const createUserScheme = z.object({
  name: z.string(),
  email: z.string().email(),
  age: z.number().min(14),
  password: z.string().min(12),
});

router.post("/user", async (req, res) => {
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
router.post("/user/session", async (req, res) => {
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

router.delete("/user/session", async (req, res) => {
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
    return res.status(500).json({ message: "Something went wrong" });
  }
});

router.post(
  "/user/me",
  isAuthenticated,
  async (req: isAuthenticatedRequest, res) => {
    return res.status(200).json({ user: req.user });
  }
);

const addAnimeFavoriteScheme = z.object({
  animeId: z.string(),
});

router.get(
  "/user/anime/scored",
  isAuthenticated,
  async (req: isAuthenticatedRequest, res) => {
    const scoredAnimes = await prisma.animeScore.findMany({
      where: {
        userId: req.user!.id        
      },
      include: {
        Anime: true
      }
    })
    return res.status(200).json({ scoredAnimes })
  }
)

router.post(
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

const animeScoreScheme = z.object({
  animeId: z.string(),
  score: z.number(),
});

router.post(
  "/user/score/anime",
  isAuthenticated,
  async (req: isAuthenticatedRequest, res) => {
    const { animeId, score } = animeScoreScheme.parse(req.body);

    try {
      const updatedAnime = await prisma.anime.update({
        where: {
          id: animeId,
        },
        data: {
          scoresByUsers: {
            create: {
              score,
              userId: req.user!.id,
            },
          },
        },
      });
      return res.status(200).json({ updatedAnime });
    } catch (error) {
      return res.status(400).json({ message: "Cannot update anime", error });
    }
  }
);

export default { router };
