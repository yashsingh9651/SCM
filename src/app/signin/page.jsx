"use client";
import React, { useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Card, Input, Button, Typography } from "@material-tailwind/react";
import { useFormik } from "formik";
import { schema } from "@/Schema/Login";
import toast, { Toaster } from "react-hot-toast";
import Loading from "@/components/Loading";
import axios from "axios";

const Page = () => {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  // Form Handling using formik.
  const form = useRef();
  const { values, handleChange, handleSubmit, errors, touched, handleBlur } =
    useFormik({
      initialValues: {
        email: "",
        password: "",
      },
      validationSchema: schema,
      onSubmit: async (values, action) => {
        setLoading(true);
        const response = await axios.post("/api/users/login", values); 
        if (response.data.success) {
          action.resetForm();
          setLoading(false);
          toast.success(response.data.message);
          router.push("/main");
        }
        else if (!response.data.success) {
          setLoading(false);
          toast.error(response.data.error);
        }
      },
    });
  return (
    <>
      <div className="flex justify-center items-center gap-24 h-screen">
        <Toaster />
        <Card color="transparent" shadow={false}>
          <Typography variant="h5" color="blue-gray">
            Log In
          </Typography>
          <Typography color="gray" className="mt-1 font-normal">
            Nice to meet you! Enter your details to Login.
          </Typography>
          <form
            onSubmit={handleSubmit}
            ref={form}
            className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96"
          >
            <div className="mb-1 flex flex-col gap-6">
              <Typography variant="h6" color="blue-gray" className="-mb-3">
                Your Email
              </Typography>
              <div className="relative">
                <Input
                  onBlur={handleBlur}
                  onChange={handleChange}
                  name="email"
                  value={values.email}
                  size="lg"
                  placeholder="name@mail.com"
                  className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
                  labelProps={{
                    className: "before:content-none after:content-none",
                  }}
                />
                {errors.email && touched.email && (
                  <p className="absolute top-3 right-2 text-red-600">
                    {errors.email}
                  </p>
                )}
              </div>
              <Typography variant="h6" color="blue-gray" className="-mb-3">
                Password
              </Typography>
              <div className="relative">
                <Input
                  onBlur={handleBlur}
                  onChange={handleChange}
                  name="password"
                  value={values.password}
                  type="password"
                  size="lg"
                  placeholder="********"
                  className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
                  labelProps={{
                    className: "before:content-none after:content-none",
                  }}
                />
                {errors.password && touched.password && (
                  <p className="absolute top-3 right-2 text-red-600">
                    {errors.password}
                  </p>
                )}
              </div>
            </div>
            {!loading ? (
              <Button type="submit" className="mt-6" fullWidth>
                Log In
              </Button>
            ) : (
              <Button className="mt-6" fullWidth>
                <Loading />
              </Button>
            )}
            <Typography color="gray" className="mt-4 text-center font-normal">
              Forgot Password?{" "}
              <Link href="/resetPass" className="font-medium text-gray-900">
                Reset Password
              </Link>
            </Typography>
          </form>
        </Card>
      </div>
    </>
  );
};
export default Page;