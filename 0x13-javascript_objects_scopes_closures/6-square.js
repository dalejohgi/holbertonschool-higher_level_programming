#!/usr/bin/node
/*
Empty class Rectangle that defines a rectangle
*/
const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c = undefined) {
    if (c === undefined) {
      this.print();
    } else {
      let vtcal;
      for (vtcal = 0; vtcal < this.height; vtcal++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
