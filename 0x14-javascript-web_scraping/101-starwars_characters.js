#!/usr/bin/node

const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const list = [];
    characters.forEach(character => {
      list.push(new Promise((resolve, reject) => {
        request.get(character, (cErr, cRes, cBody) => {
          if (cErr) {
            reject(cErr);
          } else if (cRes.statusCode === 200) {
            resolve(JSON.parse(cBody).name);
          }
        });
      }));
    });
    Promise.all(list).then(names => {
      names.forEach(name => {
        console.log(name);
      });
    });
  }
});
