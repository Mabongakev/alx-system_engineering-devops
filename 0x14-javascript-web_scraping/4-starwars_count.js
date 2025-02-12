const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
    console.error('Usage: node script.js <API_URL>');
    process.exit(1);
}

// Make a GET request
request.get(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
    }
    
    // Filter movies containing character ID 18 (Wedge Antilles)
    const wedgeMovies = body.results.filter(movie => 
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    
    console.log(wedgeMovies.length);
});
