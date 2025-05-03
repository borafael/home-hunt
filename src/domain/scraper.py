from datetime import datetime
import json
import re

from domain.listing import Listing


class Scraper:

    def scrape(self, html: str) -> Listing:
        reserved = True if "IN TRATTATIVA/SOSPESO" in html else False

        date_pattern = r"(\d{2}/\d{2}/\d{4})"
        start_date = None
        end_date = None

        pattern = rf"\(dal {date_pattern}\)"
        match = re.search(pattern, html)
        if match:
            (start_date,) = match.groups()  # Extract the captured date groups

        pattern = rf"\(dal {date_pattern} al {date_pattern}\)"
        match = re.search(pattern, html)
        if match:
            start_date, end_date = match.groups()  # Extract the captured date groups

        match = re.search(r'<script type="application\/ld\+json">(.*?)<\/script>', html, re.DOTALL)
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
                    availability=Listing.Availability(
                        datetime.strptime(start_date, "%d/%m/%Y").date() if start_date else None,
                        datetime.strptime(end_date, "%d/%m/%Y").date() if end_date else None
                    ),
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    size=area,
                    price=price,
                    status=Listing.Status.RESERVED if reserved else Listing.Status.PENDING
                )
            except json.JSONDecodeError:
                print("Error: Invalid JSON found.")
                return None                        