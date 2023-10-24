#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function doRequest (apiUrl) {
  return new Promise(function (resolve, reject) {
    request(apiUrl, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

request(apiUrl, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    for (const characterUrl of movie.characters) {
      try {
        const res = await doRequest(characterUrl);
        const person = JSON.parse(res);
        console.log(person.name);
      } catch (error) {
        console.log(error);
      }
    }
  }
});
