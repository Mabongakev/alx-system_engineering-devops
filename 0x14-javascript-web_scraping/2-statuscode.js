const request = require('request');

// Get the URL from command line arguments
const url = process.argv[2];

if (!url) {
    console.error('Usage: node script.js <URL>');
    process.exit(1);
}

// Make a GET request
request.get(url, (error, response) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }
    console.log(`code: ${response.statusCode}`);
});
