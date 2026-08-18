#!/usr/bin/node
const arr = process.argv;

arr.sort();
arr.reverse();

if (arr.length < 4) {
  console.log(0);
} else {
  console.log(arr[1]);
}
