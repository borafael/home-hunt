class ListingsMap extends HTMLElement {

  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.map = null;
  }

  connectedCallback() {
    this.render();
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          height: 100%;
          width: 100%;
        }
        #map-container {
          height: 100%;
          width: 100%;
        }
      </style>
      <div id="map-container"></div>
    `;
    this.mapContainer = this.shadowRoot.getElementById('map-container');
  }

  initializeMap() {
    if (!this.mapContainer || !window.google || !window.google.maps) {
      console.error('Google Maps API not loaded or map container not available.');
      return;
    }

    this.map = new google.maps.Map(this.mapContainer, {
      center: { lat: 45.4339, lng: 12.4078 },
      zoom: 12,
      mapTypeId: 'roadmap'
    });
  }
}

customElements.define('listings-map', ListingsMap);