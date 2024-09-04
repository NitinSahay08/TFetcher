
import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_URL = "https://tataplay-urls.vercel.app/origin.json"
RETRIES = 3

def fetch_api(url, retries):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad status codes
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching API data (attempt {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                continue
            else:
                return None

def transform_data(api_data):
    transformed_data = []

    return api_data['data']

def main():
    api_data = fetch_api(API_URL, RETRIES)
    if api_data:
        transformed_data = transform_data(api_data)
        if transformed_data:
            with open("fetcher.json", "w") as f:
                json.dump(transformed_data, f, indent=2)
                logging.info("Data saved to fetcher.json")
        else:
            logging.warning("No clear keys found in API response")
    else:
        logging.error("Failed to fetch data from API")

if __name__ == "__main__":
    main()
