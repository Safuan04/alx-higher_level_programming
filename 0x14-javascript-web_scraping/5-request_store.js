#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');
const argv = process.argv;

const WebPageURL = argv[2];
const filename = argv[3];

request(WebPageURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = body;
    fs.writeFile(filename, content, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
