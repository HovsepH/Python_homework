from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "cars.json"

def load_cars():
    """Load cars from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_cars(cars):
    """Save cars to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(cars, file, indent=4)

@app.route("/cars", methods=["GET"])
def get_cars():
    """Get the list of all cars."""
    cars = load_cars()
    return jsonify(cars), 200

@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id):
    """Get a specific car by ID."""
    cars = load_cars()
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(car), 200

@app.route("/cars", methods=["POST"])
def add_car():
    """Add a new car."""
    cars = load_cars()
    new_car = request.get_json()

    if not all(key in new_car for key in ["make", "model", "year", "price"]):
        return jsonify({"error": "Missing required car attributes"}), 400

    new_id = max((car["id"] for car in cars), default=0) + 1
    new_car["id"] = new_id
    cars.append(new_car)
    save_cars(cars)
    return jsonify(new_car), 201

@app.route("/cars/<int:car_id>", methods=["PUT"])
def update_car(car_id):
    """Update an existing car."""
    cars = load_cars()
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        return jsonify({"error": "Car not found"}), 404

    update_data = request.get_json()
    for key in ["make", "model", "year", "price"]:
        if key in update_data:
            car[key] = update_data[key]

    save_cars(cars)
    return jsonify(car), 200

@app.route("/cars/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    """Delete a car by ID."""
    cars = load_cars()
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        return jsonify({"error": "Car not found"}), 404

    cars.remove(car)
    save_cars(cars)
    return jsonify({"message": "Car deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
