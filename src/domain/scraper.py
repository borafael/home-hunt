import json
import re

from domain.listing import Listing


class Scraper:

    def scrape(self, html: str) -> Listing:
        match = re.search(r'<script type="application\/ld\+json">(.*?)<\/script>', html, re.DOTALL)

        reserved = True if "IN TRATTATIVA/SOSPESO" in html else False

        if match:
            json_text = match.group(1)  # Get the captured JSON string

            try:
                data = json.loads(json_text)  # Parse the JSON
                # Estrai i dati
                latitude = data['geo']['latitude']
                longitude = data['geo']['longitude']
                price = data['offers']['price']

                # I valori di camere da letto e bagni sono in una lista, quindi dobbiamo iterare per trovarli
                bedrooms = None
                bathrooms = None
                area = None #Inizializzo area a None
                for prop in data['additionalProperty']:
                    if prop['name'] == 'Bedrooms':
                        bedrooms = prop['value']
                    elif prop['name'] == 'Bathrooms':
                        bathrooms = prop['value']
                    elif prop['name'] == 'Area Size': #Estraggo anche l'area
                        area = prop['value']
                
                return Listing(
                    coordinates=Listing.Coordinates(latitude, longitude),
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    size=area,
                    price=price,
                    status=Listing.Status.RESERVED if reserved else Listing.Status.PENDING
                )
            except json.JSONDecodeError:
                print("Error: Invalid JSON found.")
                return None                        