import nodemailer from "nodemailer";
import User from "@/models/userModel";
import bcryptjs from "bcryptjs";

export const sendMail = async ({ email, emailType, userId }) => {
  try {
    const hashedToken = await bcryptjs.hash(userId.toString(), 10);
    if (emailType === "VERIFY") {
      await User.findByIdAndUpdate(userId, {
        verifyToken: hashedToken,
        verifyTokenExpiry: Date.now() + 3600000,
      });
    } else if (emailType === "RESET") {
      await User.findByIdAndUpdate(userId, {
        forgotPasswordToken: hashedToken,
        forgotPasswordTokenExpiry: Date.now() + 3600000,
      });
    }
    const transport = nodemailer.createTransport({
      service: "gmail",
      host: "smtp.gmail.com",
      port: 587,
      auth: {
        // add senders gmail to the .env file as NODE_USER
        user: process.env.NODE_USER,
        // Create an app on your gmail and add generated pass to the .env file as NODE_PASS
        pass: process.env.NODE_PASS,
      },
    });
    const mailOptions = {
      from: { name: "SCM", address: process.env.NODE_USER },
      to: email,
      subject: `${
        emailType === "VERIFY" ? "Verify your email" : "Reset your Password"
      }`,
      // add your domain to .env file as DOMAIN
      html: `<p>Click <a href="${process.env.DOMAIN}/${
        emailType === "VERIFY" ? "verifyemail" : "resetPass/verify"
      }?token=${hashedToken}">here</a> to${
        emailType === "VERIFY" ? "Verify your email" : "Reset your password"
      } or copy and paste the link to your browser. <br/> ${
        process.env.DOMAIN
      }/${
        emailType === "VERIFY" ? "verifyemail" : "resetPass/verify"
      }?token=${hashedToken} </p>`,
    };
    const mailResponse = await transport.sendMail(mailOptions);
    return mailResponse;
  } catch (error) {
    throw new Error(error.message);
  }
};