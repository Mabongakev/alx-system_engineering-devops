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
    
    // Compute number of completed tasks per user
    const taskCount = {};
    body.forEach(task => {
        if (task.completed) {
            taskCount[task.userId] = (taskCount[task.userId] || 0) + 1;
        }
    });
    
    // Print users with completed tasks
    console.log(taskCount);
});
