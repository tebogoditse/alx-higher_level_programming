#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'UTF8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
