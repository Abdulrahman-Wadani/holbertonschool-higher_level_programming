#!/usr/bin/node
const arr = process.argv;

let str = "";
if (!Number.isNaN(Number(arr[2]))) {
  for (let i = 0; i < (Number(arr[2]) | 0); i++) {
    for (let j = 0; j < (Number(arr[2]) | 0); j++) {
      str += 'X';
    }
    str += '\n';
  }
  console.log(str);
} else {
    console.log('Missing size');
}
