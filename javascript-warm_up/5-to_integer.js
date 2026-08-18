#!/usr/bin/node
const arr = process.argv;

arr[2] -= 0;
if (typeof arr[2] === 'number') {
  console.log('My number: ' + (arr[2] | 0));
} else {
  console.log('Not a number');
}
