#!/usr/bin/ node

const [, arg] = process.argv;
const n = parseInt(arg);

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
