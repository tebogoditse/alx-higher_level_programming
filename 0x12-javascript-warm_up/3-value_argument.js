#!/usr/bin/node

const process = require('process');

const args = process.argv.length;

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log(process.argv[2]);
}
