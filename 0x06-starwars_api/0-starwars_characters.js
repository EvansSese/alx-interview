#!/usr/bin/node

const request = require('request');

function printMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, (error, response, body) => {
        if (error || response.statusCode !== 200) {
            console.log(`Failed to retrieve movie information for Movie ID ${movieId}`);
            return;
        }

        const movieData = JSON.parse(body);
        const characters = movieData.characters;

        characters.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (error || response.statusCode !== 200) {
                    console.log(`Failed to retrieve character information for: ${characterUrl}`);
                    return;
                }

                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <Movie ID>");
    process.exit(1);
}

const movieId = process.argv[2];
printMovieCharacters(movieId);
