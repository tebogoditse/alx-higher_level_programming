#!/usr/bin/node

const process = require('process');

if (process.argv.length < 4) {
  console.log(0);
} else if (process.argv.length >= 4) {
  const list = process.argv.sort();
  list.reverse();
  console.log(list[1]);
}
