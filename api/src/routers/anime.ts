import { Router } from "express";
import { z } from "zod";
import { prisma } from "../utils/prisma";

const router = Router();

const animeScheme = z.object({
  name: z.string(),
  year: z.string(),
  season: z.string(),
  genre: z.string(),
  score: z.number(),
  synopsis: z.string().max(500),
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

router.get("/anime", async (req, res) => {
  const allAnimes = await prisma.anime.findMany({
    include: {
      Character: true,
    },
  });
  return res.status(200).json({ animes: allAnimes });
});

router.post("/anime", async (req, res) => {
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

router.get("/anime/rank", async (req, res) => {
  try {
    const rankAnimes = await prisma.anime.findMany({
      orderBy: {
        score: "desc",
      },
    });
    return res.status(200).json({ rankAnimes });
  } catch (error) {
    return res.status(400).json({ message: "Bad request error", error });
  }
});

router.post("/anime/character", async (req, res) => {
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

router.get("/anime/character", async (req, res) => {
  const allCharacter = await prisma.character.findMany({
    include: {
      animes: true,
    },
  });
  return res.status(200).json({ allCharacter });
});

export default { router }
