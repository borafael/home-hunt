import * as client from './client.js';
import * as render from './render.js';

document.addEventListener('DOMContentLoaded', async () => {
  const listingsContainer = document.getElementById('listings');

  try {
    const listings = await client.getListings();
    render.initMap(listings); // Initialize the map with the fetched listings
  } catch (error) {
    console.error('Error fetching initial listings:', error);
    render.displayErrorMessage('Failed to load listings.', listingsContainer);
  }
});