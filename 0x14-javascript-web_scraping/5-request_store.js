#!/usr/bin/node
/*
prints the title of a Star Wars movie by its id.
*/
const fs = require('fs');
const argv = process.argv.slice(2);
const request = require('request');
const url = argv[0];
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    fs.writeFile(argv[1], body, 'utf8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
