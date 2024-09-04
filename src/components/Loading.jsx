import React from "react";

const Loading = () => {
  return (
    <div className="flex flex-row gap-2 max-w-fit mx-auto py-1">
      <div className="w-4 h-4 rounded-full bg-gray-100 animate-bounce"></div>
      <div className="w-4 h-4 rounded-full bg-gray-100 animate-bounce [animation-delay:-.3s]"></div>
      <div className="w-4 h-4 rounded-full bg-gray-100 animate-bounce [animation-delay:-.5s]"></div>
    </div>
  );
};

export default Loading;