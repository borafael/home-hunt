let map;

function initMap(listings) {
  // Determine the initial center and zoom level
  let center = { lat: 45.4305, lng: 12.3296 }; // Default to Venice
  let bounds = new google.maps.LatLngBounds();

  if (listings && listings.length > 0) {
    let sumLat = 0;
    let sumLng = 0;
    listings.forEach(listing => {
      const latLng = { lat: listing.coordinates.latitude, lng: listing.coordinates.longitude };
      sumLat += latLng.lat;
      sumLng += latLng.lng;
      bounds.extend(latLng);
    });
    center = { lat: sumLat / listings.length, lng: sumLng / listings.length };
  }

  map = new google.maps.Map(document.getElementById('map'), {
    center: center,
    zoom: listings && listings.length > 0 ? undefined : 12 // Adjust default zoom
  });

  if (listings && listings.length > 0) {
    map.fitBounds(bounds); // Adjust zoom to fit all markers
  }

  addListingMarkers(listings);
};

function addListingMarkers(listings) {
  if (listings) {
    listings.forEach(listing => {
      const position = { lat: listing.coordinates.latitude, lng: listing.coordinates.longitude };
      const marker = new google.maps.Marker({
        position: position,
        map: map,
        title: `Listing ${listing.id.substring(0, 8)}...`,
      });

      const infowindow = new google.maps.InfoWindow({
        content: `<a href="${listing.link}" target="_blank">${listing.link}</a><br>Price: €${listing.price}`,
      });

      marker.addListener('click', () => {
        infowindow.open(map, marker);
      });
    });
  }
}

// This function will be called when the Google Maps API is loaded
window.initMap = initMap;

export { initMap };