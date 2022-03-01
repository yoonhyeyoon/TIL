let count = 0; // 숫자
count += 1;
// count = "갑자기 분위기 문자열"; // error

const message: string = "hello world";

const done: boolean = true;

const numbers: number[] = [1, 2, 3];
const messages: string[] = ["hello", "world"];

// messages.push(1); // error

let mightBeUndefined: string | undefined = undefined;
let nullableNumber: number | null = null;

let color: "red" | "orange" | "yellow" = "red";
color = "yellow";
// color = "green"; // error
