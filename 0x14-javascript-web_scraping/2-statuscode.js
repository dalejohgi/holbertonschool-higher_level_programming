#!/usr/bin/node
/*
Writes the content of a file.
*/
const argv = process.argv.slice(2);
const request = require('request');
request(argv[0], function (error, response) {
  if (error) {
    return console.log(error);
  } else {
    console.log('code: %d', response.statusCode);
  }
});
