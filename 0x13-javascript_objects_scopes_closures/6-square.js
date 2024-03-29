#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (typeof c === 'undefined') { c = 'X'; }
    let lines = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        lines += c;
      }
      console.log(lines);
      lines = '';
    }
  }
}

module.exports = Square;
