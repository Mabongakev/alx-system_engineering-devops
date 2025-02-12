const fs = require('fs');
const path = require('path');

// Get the file path from command line arguments
const filePath = process.argv[2];

if (!filePath) {
    console.error('Usage: node script.js <file_path>');
    process.exit(1);
}

// Resolve the absolute path
const absolutePath = path.resolve(filePath);

// Read the file
fs.readFile(absolutePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    console.log(data);
});
