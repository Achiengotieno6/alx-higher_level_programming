#!/usr/bin/node

const request = require('request');

const Url = process.argv[2];

request(Url, function (error, response, body) {
  if (!error) {
    const filmdata = JSON.parse(body).results;

    // filter movies where "Wedge Antilles" is present
    const moviesWithAntilles = filmdata.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(moviesWithAntilles);
  }
});
