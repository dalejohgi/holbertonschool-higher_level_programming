#!/usr/bin/node
/*
Writes the content of a file.
*/
const fs = require('fs');
// Rewriting the arv sintax by cutting the first 2 positions
const argv = process.argv.slice(2);
fs.writeFile(argv[0], argv[1], 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
