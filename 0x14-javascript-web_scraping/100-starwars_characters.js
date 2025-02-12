const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.error('Usage: node script.js <movie_ID>');
    process.exit(1);
}

// Construct the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request
request.get(url, { json: true }, (error, response, body) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
    }
    
    // Fetch character names
    const characterUrls = body.characters;
    characterUrls.forEach(characterUrl => {
        request.get(characterUrl, { json: true }, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error fetching character:', charError);
                return;
            }
            if (charResponse.statusCode !== 200) {
                console.error(`Error: Received status code ${charResponse.statusCode} for character`);
                return;
            }
            console.log(charBody.name);
        });
    });
});
