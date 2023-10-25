#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const fs = require('fs');

fs.readFile(argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
