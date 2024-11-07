# app.py
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

# Sample data store
data = {
    1: {"name": "Item 1"},
    2: {"name": "Item 2"}
}

@app.route('/items', methods=['POST'])
def create_item():
    new_id = max(data.keys()) + 1 if data else 1
    item = request.get_json()
    if not item or 'name' not in item:
        abort(400, description="Invalid data")
    data[new_id] = item
    return jsonify({"id": new_id, **item}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.get_json()
    if not item or 'name' not in item:
        abort(400, description="Invalid data")
    if item_id not in data:
        abort(404, description="Item not found")
    data[item_id].update(item)
    return jsonify({"id": item_id, **data[item_id]})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in data:
        abort(404, description="Item not found")
    deleted_item = data.pop(item_id)
    return jsonify({"id": item_id, **deleted_item}), 200

# For testing purpose
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data.get(item_id)
    if not item:
        abort(404, description="Item not found")
    return jsonify({"id": item_id, **item})

if __name__ == '__main__':
    app.run(debug=True)