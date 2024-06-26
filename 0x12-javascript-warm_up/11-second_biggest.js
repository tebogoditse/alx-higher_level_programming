#!/usr/bin/node

const process = require('process');

if (process.argv.length >= 4) {
  const list = process.argv.sort();
  console.log(list[list.length - 2]);
} else {
  console.log(0);
}
