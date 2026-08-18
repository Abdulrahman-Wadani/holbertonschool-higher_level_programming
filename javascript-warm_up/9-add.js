#!/usr/bin/node
function add (a, b) {
  console.log(Number(a) + Number(b));
}

const arr = process.argv;

add(arr[2], arr[3]);
