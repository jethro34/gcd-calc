from flask import Flask, request, jsonify
from math import radians, sin, cos, sqrt, atan2
HOST = '0.0.0.0'
PORT = 8000


app = Flask(__name__)

def haversine(lat1, lon1, lat2, lon2, unit="km"):
    """ Calculate great-circle distance using Haversine formula. """

    R = 6371.0 if unit == "km" else 3958.8  # Earth radius in km or miles

    # convert coordinates from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return round(distance, 2)


# GET endpoint for single distance calculation
@app.route("/calculate-distance", methods=["GET"])
def calculate_distance():
    try:
        # get data from query parameters
        lat1 = float(request.args.get("lat1"))
        lon1 = float(request.args.get("lon1"))
        lat2 = float(request.args.get("lat2"))
        lon2 = float(request.args.get("lon2"))
        unit = request.args.get("unit", "km").lower()   # default to km

        if unit not in ["km", "miles"]:
            return jsonify({"error": "Invalid unit. Use 'km' or 'miles'."}), 400

        # calculate distance
        distance = haversine(lat1, lon1, lat2, lon2, unit)

        return jsonify({"distance": distance, "unit": unit})

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid parameters. Ensure all values are numbers."}), 400


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
