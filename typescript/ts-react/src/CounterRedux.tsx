import React, { useReducer } from "react";

type Action = { type: "INCREASE" } | { type: "DECREASE" }; // 이렇게 액션을 | 으로 연달아서 쭉 나열

// 현재 상태와 액션 객체를 파라미터로 받아와서 새로운 상태를 반환해줌
// 액션: 업데이트를 위한 정보
function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "INCREASE":
      return state + 1;
    case "DECREASE":
      return state - 1;
    default:
      throw new Error("Unhandled action");
  }
}

function Counter() {
  //const [state, dispatch] = useReducer(reducer, initialState);
  // dispatch: 액션을 발생시키는 함수
  const [count, dispatch] = useReducer(reducer, 0);
  const onIncrease = () => dispatch({ type: "INCREASE" });
  const onDecrease = () => dispatch({ type: "DECREASE" });

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
