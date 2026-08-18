#!/usr/bin/node
const arr = process.argv;

if (!Number.isNaN(Number(arr[2]))) {
  for (let i = 0; i < (Number(arr[2]) | 0); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
