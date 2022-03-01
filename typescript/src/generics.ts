// function merge(a: any, b: any): any {
//   return {
//     ...a,
//     ...b
//   };
// }

// const merged = merge({ foo: 1 }, { bar: 1 });

function merge<A, B>(a: A, b: B): A & B {
  return {
    ...a,
    ...b,
  };
}

const merged = merge({ foo: 1 }, { bar: 1 });
