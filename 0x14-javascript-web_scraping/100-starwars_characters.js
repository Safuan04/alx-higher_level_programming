#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const i of characters) {
    request(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
