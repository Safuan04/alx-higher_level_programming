#!/usr/bin/node

const process = require('process');
const request = require('request');
const argv = process.argv;

const URL = argv[2];
request(URL, (error, response) => {
  if (error) {
    console.error('code:', response.statusCode);
  }
  console.log('code:', response.statusCode);
});
