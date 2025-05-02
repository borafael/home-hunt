async function getListings() {
    try {
        const response = await fetch('http://127.0.0.1:8000/listings');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const listings = await response.json();
        const filteredListings = listings.filter(listing => listing.status !== 'RESERVED' && listing.status !== 'REJECTED');
        return filteredListings
    } catch (error) {
        console.error('Error fetching listings:', error);
        listingsContainer.innerHTML = '<p>Failed to load listings.</p>';
    }
}

export {getListings}