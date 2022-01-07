import Button from "./Button"
import styles from "./App.module.css"
import { useState,useEffect } from "react";

function App() {
  const [counter, setValue] = useState(0) 
  const [keyword, setKeyword] = useState("")
  const onClick = () => setValue((prev) => prev+1)
  const onChange = (event) => setKeyword(event.target.value)
  console.log("run")
  const iRunOnlyOnce = () => {
    console.log("only one")
  }
  useEffect(iRunOnlyOnce, [])

  return (
    <div>
      <input value={keyword} onChange={onChange} type="text" />
      <h1 className={styles.title}>{counter}</h1>
      <button onClick={onClick}>click me</button>
      <Button text={"Continue"}/>
    </div>
  );
}

export default App;
