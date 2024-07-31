#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    let i = 0;
    while (i < res.length) {
      if (res[i].completed === true) {
        if (dict[res[i].userId] === undefined) {
          dict[res[i].userId] = 1;
        } else {
          dict[res[i].userId] += 1;
        }
      }
      i++;
    }
    console.log(dict);
  }
});
