import { connect } from "@/dbConfig/dbConfig";
import User from "@/models/userModel";
import { NextResponse } from "next/server";
import bcryptjs from "bcryptjs";
import jwt from "jsonwebtoken";
connect();

export async function POST(request) {
  try {
    const reqBody = await request.json();
    const { email, password } = reqBody;
    //check if user already exists
    const user = await User.findOne({ email });
    if (!user) {
      return NextResponse.json(
        { error: "User does not exists",
        success: false }
      );
    }
    // check if password is correct
    const validPassword = await bcryptjs.compare(password, user.password);
    if (!validPassword) {
      return NextResponse.json({ error: "Invalid password",
      success: false });
    }
    // Create Token data
    const tokenData = {
      id: user._id,
      email: user.email,
    };
    // Create Token
    // Add JWT_SECRET to .env file
    const token = await jwt.sign(tokenData, process.env.JWT_SECRET, {
      expiresIn: "30d",
    });
    const response = NextResponse.json({
      message: "Login Successful",
      success: true,
    });
    response.cookies.set("token", token, {
      httpOnly: true,
    });
    return response;
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}