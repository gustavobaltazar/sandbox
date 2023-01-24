import express from "express";
import cors from "cors";
import animeRouter from './routers/anime'
import userRouter from './routers/user'

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  return res.status(200).json({ message: "Hello World!" });
});

app.use("/", animeRouter.router);
app.use("/", userRouter.router);

app.listen(4000, () => {
  console.log("Server running on port 4000");
});
