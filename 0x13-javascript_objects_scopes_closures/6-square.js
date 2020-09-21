#!/usr/bin/node
/*
Empty class Rectangle that defines a rectangle
*/
const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c = '') {
    if (c === 'C') {
      let vtcal;
      for (vtcal = 0; vtcal < this.height; vtcal++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
