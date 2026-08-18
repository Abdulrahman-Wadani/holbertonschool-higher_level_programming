#!/usr/bin/node
const arr = process.argv;

arr.sort((a, b) => b - a);

if (arr.length < 4) {
  console.log(0);
} else {
  console.log(arr[3]);
}
