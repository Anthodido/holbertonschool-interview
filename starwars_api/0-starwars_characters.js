#!/usr/bin/node
 
const request = require('request');
 
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}/`;
 
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
 
  const film = JSON.parse(body);
  const characterUrls = film.characters;
 
  const promises = characterUrls.map((url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) reject(err);
        else resolve(JSON.parse(body).name);
      });
    });
  });
 
  Promise.all(promises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((err) => console.error(err));
});
