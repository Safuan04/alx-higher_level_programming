#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const fs = require('fs');

const filename = argv[2];
const text = argv[3];
fs.writeFile(filename, text, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
