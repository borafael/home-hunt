#!/bin/bash

target_url="https://www.venice-cera.it/immobili-in-locazione-a-venezia/"
api_endpoint="http://127.0.0.1:8000/listings/"  # Replace with the actual API endpoint
api_token="YOUR_API_TOKEN_HERE"      # Replace with your API authentication token (if needed)

# Fetch URLs, extract, sort, and get unique values
urls=$(curl -s "$target_url" | grep -o 'https:\/\/www\.venice-cera\.it\/property\/[^"]*' | sort | uniq)

if [ -n "$urls" ]; then
  echo "Found the following unique property URLs. Posting to API..."
  while IFS= read -r single_url; do
    echo "Processing URL: $single_url"

    # Construct the JSON payload
    post_data=$(jq -n --arg link "$single_url" '{ "link": $link }')

    # Make the POST request using curl
    response=$(curl -s -X POST \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $api_token" \
      -d "$post_data" \
      "$api_endpoint")

    # You can process the API response here if needed
    echo "API Response for $single_url: $response"
    echo "" # Add a newline for better readability

    # Optional: Add a delay between requests
    # sleep 1
  done <<< "$urls"
else
  echo "No matching property URLs found on $target_url"
fi

exit 0