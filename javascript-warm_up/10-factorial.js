#!/usr/bin/node
function factorial (a) {
  if (Number.isNaN(a) || a <= 1) {
    return 1;
  }
  return factorial(a - 1) * a;
}

const arr = process.argv;

console.log(factorial(Number(arr[2])));
