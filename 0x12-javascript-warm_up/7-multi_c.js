#!/usr/bin/node

const args = process.argv;

let num = parseInt(argv[2]);

if (isNaN(num) || args.length < 3) {
  console.log('Missing number of occurrences');
}
while (num > 0) {
  console.log('C is fun');
  num -= 1;
}
