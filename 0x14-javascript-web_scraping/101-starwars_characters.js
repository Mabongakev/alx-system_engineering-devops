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
request.get(url, { json: true }, async (error, response, body) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
    }
    
    // Fetch character names in order
    const characterUrls = body.characters;
    try {
        for (const characterUrl of characterUrls) {
            await new Promise((resolve, reject) => {
                request.get(characterUrl, { json: true }, (charError, charResponse, charBody) => {
                    if (charError) {
                        console.error('Error fetching character:', charError);
                        reject(charError);
                        return;
                    }
                    if (charResponse.statusCode !== 200) {
                        console.error(`Error: Received status code ${charResponse.statusCode} for character`);
                        reject(new Error('Invalid status code'));
                        return;
                    }
                    console.log(charBody.name);
                    resolve();
                });
            });
        }
    } catch (err) {
        console.error('Error processing characters:', err);
    }
});
