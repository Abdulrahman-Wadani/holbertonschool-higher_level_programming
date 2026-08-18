#!/usr/bin/node
const arr = process.argv;

if (!Number.isNaN(Number(arr[2]))) {
  console.log('My number: ' + (arr[2] | 0));
} else {
  console.log('Not a number');
}
