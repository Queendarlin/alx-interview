#!/usr/bin/node

const request = require('request');

// Function to get Star Wars characters
function getStarWarsCharacters (movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  // Fetch the movie data
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }

    // Check if the response status code is 200 (OK)
    if (response.statusCode !== 200) {
      console.error('Failed to fetch movie data:', response.statusCode);
      return;
    }

    // Parse the JSON response
    const data = JSON.parse(body);

    // Get the array of character URLs from the movie data
    const characters = data.characters;

    // Function to fetch character data
    function fetchCharacter (characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            reject(characterError);
            return;
          }

          if (characterResponse.statusCode !== 200) {
            reject(new Error(`Failed to fetch character data: ${characterResponse.statusCode}`));
            return;
          }

          const characterData = JSON.parse(characterBody);
          resolve(characterData.name);
        });
      });
    }

    // Fetch all characters' data
    const promises = characters.map(url => fetchCharacter(url));

    // Resolve all promises and print character names
    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error('Error fetching characters:', error);
      });
  });
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if a movie ID was provided
if (movieId) {
  // Call the function to fetch and display the characters
  getStarWarsCharacters(movieId);
} else {
  // Log a message if no movie ID was provided
  console.log('Please provide a movie ID as a command-line argument.');
}
