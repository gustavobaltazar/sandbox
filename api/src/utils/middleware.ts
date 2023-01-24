import { NextFunction, Request, Response } from "express";
import { z } from "zod";
import { prisma } from "./prisma";
import { User } from "@prisma/client";

export interface isAuthenticatedRequest extends Request{
    user?: User;
}

const isAuthenticatedScheme = z.object({
    sessionId: z.string(),
  });
  
export const isAuthenticated = async (
    req: isAuthenticatedRequest,
    res: Response,
    next: NextFunction
  ) => {
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
      next();
    } catch (error) {
      return res.status(400).json({ message: "UNATHORIZED" });
    }
  };