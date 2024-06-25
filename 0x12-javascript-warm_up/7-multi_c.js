#!/usr/bin/node

const x = Number(process.argv[2]);

if (!isNaN(x)) {
  let i = 0;
  for (; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
