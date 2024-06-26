#!/usr/bin/node

const process = require('process');

function factorial (num) {
  if (num === 0) {
    return 1;
  } else if ((isNaN(num)) || (num === 1)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(Number(process.argv[2])));
