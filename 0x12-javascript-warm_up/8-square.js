#!/usr/bin/node

const args = process.argv;

const num = parseInt(args[2]);

let lines = '';

if (isNaN(num) || args.length < 3) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  for (let j = 0; j < num; j++) {
    lines += 'X';
  }
  console.log(lines);
  lines = '';
}
