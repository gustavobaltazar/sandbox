import express from 'express'
import { z } from 'zod'
import { prisma } from './utils/prisma';

const app = express();

app.use(express.json())

app.get("/", (req, res) => {
    return res.json({ message: "Deu certo" })
})

const createAnimeScheme = z.object({
    name: z.string(),
    year: z.string()
})

app.get("/anime", async (req, res) => {
    const animes = await prisma.anime.findMany()
    return res.json({ message: "Deu certo", animes })
})

app.post("/anime", async (req, res) => {
    console.log("body da request:", req.body);
    try {
        const anime = createAnimeScheme.parse(req.body);
        const createdAnime = await prisma.anime.create({
            data: anime
        })
        return res.json({ message: "Deu certo", anime: createdAnime })
    } catch (error) {
        return res.status(400).json({ message: "Deu errado", error })
    }
})

app.listen(3000, () => {
    console.log("Server running in port 3000")
})
