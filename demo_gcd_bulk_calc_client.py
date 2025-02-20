import requests

BULK_DIST_URL = "http://127.0.0.1:8000"
# BULK_DIST_URL = "https://gcd-calculator-242741576992.us-west1.run.app"
BULK_DIST_ENDPOINT = "/bulk-distances"

payload = {
    "coordinate_pairs": [
        {
            "lat1": 43.0481,    # Syracuse, NY latitude
            "lon1": -76.1474,   # Syracuse, NY longitude
            "lat2": 42.8864,    # Buffalo, NY latitude
            "lon2": -78.8784,   # Buffalo, NY longitude
        },
        {
            "lat1": 43.0481,    # Syracuse, NY latitude
            "lon1": -76.1474,   # Syracuse, NY longitude
            "lat2": 42.6526,    # Albany, NY latitude
            "lon2": -73.7562,   # Albany, NY longitude
        }
    ],
    # "unit": "miles"
}

print("\033c", end="")  # clear screen
print("\nSending POST request with payload:\n\t", payload)

response = requests.post(BULK_DIST_URL + BULK_DIST_ENDPOINT, json=payload)
print("\nResponse received:\n\t", response.json(), "\n")
