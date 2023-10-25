#!/usr/bin/node

const process = require('process');
const request = require('request');
const argv = process.argv;

const StarWarsURL = argv[2];

request(StarWarsURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let counter = 0;
    const StarWarsData = JSON.parse(body);
    for (const film of StarWarsData.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
