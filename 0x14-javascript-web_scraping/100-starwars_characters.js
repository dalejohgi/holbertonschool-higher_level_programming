#!/usr/bin/node
/*
prints the title of a Star Wars movie by its id.
*/
const argv = process.argv.slice(2);
const request = require('request');
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + argv[0];
request(filmUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const film = JSON.parse(body);
    for (const charUrl of film.characters) {
      request(charUrl, function (error, response, body) {
        if (error) {
          return console.log(error);
        } else {
          const char = JSON.parse(body);
          console.log(char.name);
        }
      });
    }
  }
});
