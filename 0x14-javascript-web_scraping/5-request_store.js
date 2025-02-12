const request = require('request');
const fs = require('fs');
const path = require('path');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
    console.error('Usage: node script.js <URL> <file_path>');
    process.exit(1);
}

// Resolve the absolute path
const absolutePath = path.resolve(filePath);

// Make a GET request
request.get(url, (error, response, body) => {
    if (error) {
        console.error('Error making request:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error: Received status code ${response.statusCode}`);
        return;
    }
    
    // Write response body to file
    fs.writeFile(absolutePath, body, 'utf8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return;
        }
        console.log('File saved successfully');
    });
});

