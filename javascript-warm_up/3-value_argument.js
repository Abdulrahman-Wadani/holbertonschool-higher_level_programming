#!/usr/bin/node
const arr = process.argv;

if (!arr[2]) {
  console.log('No argument');
} else {
  console.log(arr[2]);
}
