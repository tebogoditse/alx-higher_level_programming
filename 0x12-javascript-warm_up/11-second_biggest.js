#!/usr/bin/node

const process = require('process');

if (process.argv.length >= 4) {
  const list = process.argv.sort();
  list.reverse();
  console.log(list[1]);
} else {
  console.log(0);
}
