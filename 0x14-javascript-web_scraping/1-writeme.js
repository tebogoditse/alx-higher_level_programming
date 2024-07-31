#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(path, stringToWrite, 'UTF8', err => {
  if (err) {
    console.log(err);
  }
});
