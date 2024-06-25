#!/usr/bin/node

const size = Number(process.argv[2]);

if (!isNaN(size)) {
  let i = 0;
  for (; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
