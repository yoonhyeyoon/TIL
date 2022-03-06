import React from "react";
import Counter from "./Counter";
import Greetings from "./Greetings";
import MyForm from "./MyForm";
import ReducerSample from "./ReducerSample";

const App: React.FC = () => {
  const onClick = (name: string) => {
    console.log(`${name} says hello`);
  };

  const onSubmit = (form: { name: string; description: string }) => {
    console.log(form);
  };
  return (
    <>
      <Greetings name="Hello" onClick={onClick} />
      <Counter />
      <MyForm onSubmit={onSubmit} />
      <ReducerSample />
    </>
  );
};

export default App;
