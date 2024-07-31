#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
    if (err) {
        return console.log(err);
    }

    if (res.statusCode !== 200) {
        return console.log(`Error: Unable to fetch data for movie ID ${movieId}`);
    }

    const characters = body.characters;

    characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (err, res, body) => {
            if (err) {
                return console.log(err);
            }

            if (res.statusCode === 200) {
                console.log(body.name);
            } else {
                console.log(`Error: Unable to fetch character data from ${characterUrl}`);
            }
        });
    });
});
