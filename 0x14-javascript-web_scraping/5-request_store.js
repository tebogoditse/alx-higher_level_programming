#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (_err, data, body) => {
  fs.writeFile(path, body, 'UTF8', err => {
    if (err) {
      console.log(err);
    }
  });
});
