from flask import Blueprint, request, jsonify
from app import db

rooms_bp = Blueprint('rooms', __name__)

# Create a new room
@rooms_bp.route('/rooms', methods=['POST'])
def create_room():
    data = request.get_json()
    query = """
        INSERT INTO Rooms (room_number, capacity, price, is_extendable, view_types, amenities, problems, hotel_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """
    result = db.engine.execute(query, (
        data['room_number'], data['capacity'], data['price'], data['is_extendable'],
        data.get('view_types'), data['amenities'], data.get('problems'), data['hotel_id']
    ))
    room_id = result.fetchone()[0]
    return jsonify({"message": "Room created", "id": room_id}), 201

# Get all rooms
@rooms_bp.route('/rooms', methods=['GET'])
def get_rooms():
    query = "SELECT id, room_number, capacity, price, is_extendable, view_types, amenities, problems, hotel_id FROM Rooms;"
    result = db.engine.execute(query)
    rooms = [dict(row) for row in result]
    return jsonify(rooms), 200

# Get a specific room by ID
@rooms_bp.route('/rooms/<int:id>', methods=['GET'])
def get_room(id):
    query = "SELECT id, room_number, capacity, price, is_extendable, view_types, amenities, problems, hotel_id FROM Rooms WHERE id = %s;"
    result = db.engine.execute(query, (id,))
    room = result.fetchone()
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(dict(room)), 200

# Update a room
@rooms_bp.route('/rooms/<int:id>', methods=['PUT'])
def update_room(id):
    data = request.get_json()
    query = """
        UPDATE Rooms
        SET room_number = %s, capacity = %s, price = %s, is_extendable = %s, view_types = %s, amenities = %s, problems = %s, hotel_id = %s
        WHERE id = %s;
    """
    db.engine.execute(query, (
        data.get('room_number'), data.get('capacity'), data.get('price'), data.get('is_extendable'),
        data.get('view_types'), data.get('amenities'), data.get('problems'), data.get('hotel_id'), id
    ))
    return jsonify({"message": "Room updated"}), 200

# Delete a room
@rooms_bp.route('/rooms/<int:id>', methods=['DELETE'])
def delete_room(id):
    query = "DELETE FROM Rooms WHERE id = %s;"
    db.engine.execute(query, (id,))
    return jsonify({"message": "Room deleted"}), 200