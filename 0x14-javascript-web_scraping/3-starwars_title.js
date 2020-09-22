#!/usr/bin/node
/*
prints the title of a Star Wars movie by its id.
*/
const argv = process.argv.slice(2);
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + argv[0];
request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
