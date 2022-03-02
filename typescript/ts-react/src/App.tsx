import React from "react";
import Counter from "./Counter";
import Greetings from "./Greetings";

const App: React.FC = () => {
  const onClick = (name: string) => {
    console.log(`${name} says hello`);
  };
  return (
    <>
      <Greetings name="Hello" onClick={onClick} />
      <Counter />
    </>
  );
};

export default App;
