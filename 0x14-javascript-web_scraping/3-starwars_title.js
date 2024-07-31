#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const uri = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(uri, (_err, _res, body) => {
  console.log(JSON.parse(body).title);
});
