import requests

SINGLE_DIST_URL = "http://127.0.0.1:8000"
# SINGLE_DIST_URL = "https://gcd-calculator-242741576992.us-west1.run.app"
SINGLE_DIST_ENDPOINT = "/single-distance"

params = {
    "lat1": 43.0481,    # Syracuse, NY latitude
    "lon1": -76.1474,   # Syracuse, NY longitude
    "lat2": 42.8864,    # Buffalo, NY latitude
    "lon2": -78.8784,   # Buffalo, NY longitude
    # "unit": "miles",     # optional, defaults to km if not set
    # "unit": "km"
}

print("\033c", end="")  # clear screen
print("\nSending GET request with parameters:\n\t", params)

response = requests.get(SINGLE_DIST_URL + SINGLE_DIST_ENDPOINT, params=params)
print("\nResponse received:\n\t", response.json(), "\n")
