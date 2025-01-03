from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for demonstration purposes
items = [
    # {"temperature": 645,
    # "humidity": data["humidity"],
    # "pressure": data["pressure"],
    # "light_intensity": data["light_intensity"],
    # "device_status": data["device_status"],
    # "timestamp": data["timestamp"]
    # }
]

# Helper function to find an item by ID
def find_item(item_id):
    return next((item for item in items if item["id"] == item_id), None)

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

# Get all items
@app.route("/iot", methods=["GET"])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Create a new item
@app.route("/iot", methods=["POST"])
def create_item():
    data = request.get_json()

    new_item = {
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "pressure": data["pressure"],
        "light_intensity": data["light_intensity"],
        "device_status": data["device_status"],
        "timestamp": data["timestamp"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    if "name" in data:
        item["name"] = data["name"]
    if "price" in data:
        item["price"] = data["price"]

    return jsonify(item)

# Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
