# gcd-calc microservice
Great-circle distance calculator:
Given the latitude and longitude of a pair (or pairs) of points and a unit (km or miles),
return the great-circle distance between them
(if no unit is provided, the distance will be given in km).

How to request data:
  - For single-distance calculation (one distance between two points):
    <br>Make an HTTP GET request to https://gcd-calculator-242741576992.us-west1.run.app/single-distance
    <br>with a JSON dict with keys: lat1, lon1, lat2, lon2, unit (optional). Query parameters are sent in the URL.

    Example call (python):
```python
params = {"lat1": 43.0481, "lon1": -76.1474, "lat2": 42.8864, "lon2": -78.8784, "unit": "km"}
response = requests.get("https://gcd-calculator-242741576992.us-west1.run.app/single-distance", params=params)
```

  - For bulk-distance calculation (distances between pairs of points):
    <br>Make an HTTP POST request to https://gcd-calculator-242741576992.us-west1.run.app/bulk-distances
    <br>with a JSON dict with keys: coordinate_pairs, unit (optional); where coordinate_pairs is a list of dict with keys: lat1, lon1, lat2, lon2.
    <br>JSON goes in the payload.

    Example call (python):
```python
payload = {
  "coordinate_pairs": [
    {"lat1": 43.0481, "lon1": -76.1474, "lat2": 42.8864, "lon2": -78.8784},
    {"lat1": 43.0481, "lon1": -76.1474, "lat2": 42.6526, "lon2": -73.7562}
  ],
  "unit": "miles"
}
response = requests.post("https://gcd-calculator-242741576992.us-west1.run.app/bulk-distances", json=payload)
```
  
How to receive data:
  - For single-distance calculation:
    <br>The GET request response contains a JSON dictionary with keys: "distance" and "unit":

```json
{
  "distance": 238.5,
  "unit": "km"
}
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Example call (python):
```python
response = requests.get("https://gcd-calculator-242741576992.us-west1.run.app/single-distance", params=params)
distance = response.json()["distance"]  # float
unit = response.json()["unit"]  # string
```
  
  - For bulk-distance calculation:
    <br>The POST request response contains a JSON dictionary with keys: "distances" and "unit",
    <br>where "distances" is a list of floats:
```json
{
  "distances": [238.5, 325.2],
  "unit": "miles"
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Example call (python):
```python
response = requests.post("https://gcd-calculator-242741576992.us-west1.run.app/bulk-distances", json=params)
distances = response.json()["distances"]  # list of floats
unit = response.json()["unit"]  # string
```

[UML Sequence Diagram](/trianaj_cs361_A8_uml.png)
