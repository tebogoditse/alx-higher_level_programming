#!/usr/bin/node

const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    let i = 0;
    const characters = JSON.parse(body).characters;
    while (i < characters.length) {
      request(characters[i], (cErr, cRes, cBody) => {
        if (cErr) {
          console.log(cErr);
        } else {
          console.log(JSON.parse(cBody).name);
        }
      });
      i++;
    }
  }
});
