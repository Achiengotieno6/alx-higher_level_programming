#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const ApiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const printCharacter = function (characterUrl) {
  request(characterUrl, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const person = JSON.parse(body);
      console.log(person.name);
    }
  });
};

request(ApiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    for (const characterUrl of movie.characters) {
      printCharacter(characterUrl);
    }
  }
});
