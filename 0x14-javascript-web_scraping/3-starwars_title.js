#!/usr/bin/node

const process = require('process');
const request = require('request');
const argv = process.argv;

const MovieURL = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(MovieURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const MovieTitle = JSON.parse(body);
    console.log(MovieTitle.title);
  }
});
