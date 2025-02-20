# gcd-calc microservice
Great-circle distance calculator:
Given the latitude and longitude of a pair (or pairs) of points, return the great-circle distance between them.
It supports km and miles. If no unit is provided, it defaults to km.

How to request data:
  - For single-distance calculation (one distance between two points):
    Make an HTTP GET request
    to https://gcd-calculator-242741576992.us-west1.run.app/single-distance
    with a JSON dict with keys: lat1, lon1, lat2, lon2, unit (optional)
    JSON goes in the headers

    Example call: (in python)
      params = {
        "lat1": 43.0481,    # Syracuse, NY latitude
        "lon1": -76.1474,   # Syracuse, NY longitude
        "lat2": 42.8864,    # Buffalo, NY latitude
        "lon2": -78.8784,   # Buffalo, NY longitude
        "unit": "km"
      }
      response = requests.get(https://gcd-calculator-242741576992.us-west1.run.app/single-distance, params=params)

  - For bulk-distance calculation (distances between pairs of points):
    Make an HTTP POST request
    to https://gcd-calculator-242741576992.us-west1.run.app/bulk-distances
    with a JSON dict with keys: coordinate_pairs, unit (optional);
    where coordinate_pairs is a list of pairs of points: : [{lat1, lon1, lat2, lon2}, {lat3, lon3, lat4, lon4}, {etc.}]
    JSON goes in the payload

    Example call: (in python)
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
        "unit": "miles"
      }
      response = requests.post(https://gcd-calculator-242741576992.us-west1.run.app/bulk-distances, json=payload)
  
How to receive data:
  - For single-distance calculation:
    The GET request response contains a JSON dictionary with keys: "distance" and "unit"

    Example:
      response = requests.get(https://gcd-calculator-242741576992.us-west1.run.app/single-distance, params=params)
      distance = response.json()["distance"]  # float
      unit = response.json()["unit"]  # string
  
  - For bulk-distance calculation:
    The POST request response contains a JSON dictionary with keys: "distances" and "unit"

    Example:
      response = requests.post(https://gcd-calculator-242741576992.us-west1.run.app/bulk-distances, json=params)
      distances = response.json()["distances"]  # list of floats
      unit = response.json()["unit"]  # string

[UML Sequence Diagram:](/trianaj_cs361_A8_UML.png)