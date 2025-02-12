const fs = require('fs');
const path = require('path');

// Get the file path and content from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
    console.error('Usage: node script.js <file_path> <content>');
    process.exit(1);
}

// Resolve the absolute path
const absolutePath = path.resolve(filePath);

// Write the file
fs.writeFile(absolutePath, content, 'utf8', (err) => {
    if (err) {
        console.error('Error writing file:', err);
        return;
    }
    console.log('File written successfully');
