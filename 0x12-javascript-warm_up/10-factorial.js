#!/usr/bin/node
function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
const number = parseInt(process.argv[2]);
if (number) {
  const result = factorial(number);
  console.log(result);
} else {
  console.log(1);
}
