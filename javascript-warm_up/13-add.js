#!/usr/bin/node
function add (a, b) {
  console.log(Number(a) + Number(b));
}

module.exports = {
  add: add()
};
