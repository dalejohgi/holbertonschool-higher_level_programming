#!/usr/bin/node
/*
prints the title of a Star Wars movie by its id.
*/
const argv = process.argv.slice(2);
const request = require('request');
const apiUrl = argv[0];
request(apiUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const doneTasks = {};
    const jsonObj = JSON.parse(body);
    for (const obj of jsonObj) {
      if (obj.completed === true) {
        if (doneTasks[obj.userId] === undefined) {
          doneTasks[obj.userId] = 0;
        }
        doneTasks[obj.userId]++;
      }
    }
    console.log(doneTasks);
  }
});
