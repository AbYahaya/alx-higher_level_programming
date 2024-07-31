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
    
    // Function to fetch and print character names sequentially
    const fetchCharacterNames = (index) => {
        if (index >= characters.length) {
            return;
        }
        
        request(characters[index], { json: true }, (err, res, body) => {
            if (err) {
                return console.log(err);
            }
            
            if (res.statusCode === 200) {
                console.log(body.name);
                fetchCharacterNames(index + 1);
            } else {
                console.log(`Error: Unable to fetch character data from ${characters[index]}`);
            }
        });
    };
    
    // Start fetching character names
    fetchCharacterNames(0);
});
