// 상태관리

import React, { useState } from "react";

// type Information = { name: string; description: string };

function Counter() {
  const [count, setCount] = useState<number>(0); // Generics를 사용하지 않아도 무방
  // 주로 null 일수도 있고 아닐 수 도 있을 때 활용
  // const [info, setInformation] = useState<Information | null>(null);

  const onIncrease = () => setCount(count + 1);
  const onDecrease = () => setCount(count - 1);
  return (
    <div>
      <h1>{count}</h1>
      <div>
        <button onClick={onIncrease}>+1</button>
        <button onClick={onDecrease}>-1</button>
      </div>
    </div>
  );
}

export default Counter;
