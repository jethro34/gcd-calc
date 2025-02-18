# for Google Cloud deployment
from flask import Flask, request, jsonify
from math import radians, sin, cos, sqrt, atan2

HOST = "0.0.0.0"
PORT = 8000

app = Flask(__name__)

def haversine(lat1, lon1, lat2, lon2, unit="km"):
    """ Calculate great-circle distance using Haversine formula. """

    radius = 6371.0 if unit == "km" else 3958.8  # Earth radius in km or miles

    # convert coordinates from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c

    return round(distance, 2)


# GET endpoint for single distance calculation
@app.route("/single-distance", methods=["GET"])
def calculate_single_distance():
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

        response_data = {"distance": distance, "unit": unit}
        return jsonify(response_data), 200

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameter(s)."}), 400


# POST endpoint for bulk distance calculation
@app.route("/bulk-distances", methods=["POST"])
def calculate_bulk_distances():
    distances = []
    try:
        coord_pairs = request.json.get("coordinate_pairs")
        unit = request.json.get("unit", "km").lower()   # default to km

        if not coord_pairs or coord_pairs == []:
            return jsonify({"error": "No or empty request body."}), 400

        if unit not in ["km", "miles"]:
            return jsonify({"error": "Invalid unit. Use 'km' or 'miles'."}), 400

        for coord_pair in coord_pairs:
            # get data from query parameters
            lat1 = float(coord_pair.get("lat1"))
            lon1 = float(coord_pair.get("lon1"))
            lat2 = float(coord_pair.get("lat2"))
            lon2 = float(coord_pair.get("lon2"))

            # calculate distance
            distance = haversine(lat1, lon1, lat2, lon2, unit)

            distances.append(distance)

        response_data = {"distances": distances, "unit": unit}
        return jsonify(response_data), 200

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters."}), 400


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
