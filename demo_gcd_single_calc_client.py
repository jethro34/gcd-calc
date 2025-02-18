import requests

SINGLE_DIST_URL = "http://127.0.0.1:8000/single-distance"
# SINGLE_DIST_URL = "https://gcdcalculator-1045695994299.us-east4.run.app/single-distance"

params = {
    "lat1": 43.0481,    # Syracuse, NY latitude
    "lon1": -76.1474,   # Syracuse, NY longitude
    "lat2": 42.8864,    # Buffalo, NY latitude
    "lon2": -78.8784,   # Buffalo, NY longitude
    # "unit": "miles",     # optional, defaults to km if not set
    # "unit": "km"
}

print("\nSending GET request with parameters:\n\t", params)

response = requests.get(SINGLE_DIST_URL, params=params)
print("\nResponse received:\n\t", response.json())
