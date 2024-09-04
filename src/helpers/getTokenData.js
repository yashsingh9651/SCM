import jwt from "jsonwebtoken";

export const getTokenData = (req ) => {
  try {
    const token = req.cookies.get("token")?.value || "";
    // add jwt secret to .env file as JWT_SECRET
    const decodedToken = jwt.verify(token,process.env.JWT_SECRET);
    return decodedToken.id;
  } catch (error) {
    throw new Error(error.message);
  }
}