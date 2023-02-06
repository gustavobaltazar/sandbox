import { prisma } from "../src/utils/prisma";

async function seed() {
    await prisma.session.deleteMany();
    await prisma.user.deleteMany();
    await prisma.character.deleteMany();
    await prisma.anime.deleteMany();

    await prisma.user.create({
        data: {
            name: "Celso",
            age: 22,
            email: "celso@gmail.com",
            passwordHash: "celsograudo123",
        }
    })
    
    await prisma.user.create({
        data: {
            name: "Prats",
            age: 14,
            email: "prates@gmail.com",
            passwordHash: "viniciusprates15123",
        }
    })
    
    await prisma.anime.create({
        data: {
            name: "Naruto",
            genre: "Shounen",
            score: 7.5,
            season: "Fall",
            year: "2002",
            synopsis: "simsismsim"
        }
    })
    
    await prisma.anime.create({
        data: {
            name: "Bleach",
            genre: "Shounen",
            score: 8,
            season: "Spring",
            year: "2004",
            synopsis: "simsismsim"
        }
    })
    
    await prisma.anime.create({
        data: {
            name: "Renai Flops",
            genre: "Romance",
            score: 10,
            season: "Fall",
            year: "2022",
            synopsis: "simsismsim"
        }
    })
}

seed()
