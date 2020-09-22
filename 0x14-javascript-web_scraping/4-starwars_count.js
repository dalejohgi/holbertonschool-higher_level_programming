#!/usr/bin/node
/*
prints the title of a Star Wars movie by its id.
*/
const argv = process.argv.slice(2);
const request = require('request');
const apiUrl = argv[0];
const charUrl = 'https://swapi-api.hbtn.io/api/people/18/';
let counter = 0;
request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const jsonObj = JSON.parse(body);
    for (const obj of jsonObj.results) {
      if (obj.characters.includes(charUrl)) {
        counter++;
      }
    }
    console.log(counter);
  }
});
