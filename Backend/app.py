from flask import Flask, jsonify, request
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Define endpoint to retrieve all persons
@app.route('/persons', methods=['GET'])
def get():
    return jsonify([person.__dict__ for person in persons])

# Define endpoint to retrieve a specific person by ID
@app.route('/persons/<int:person_id>', methods=['GET'])
def geti(person_id):
    person = next((p for p in persons if p.id == person_id), None)
    if person:
        return jsonify(person.__dict__)
    else:
        return jsonify({'error': 'not found'})

# Define endpoint to create a new person
@app.route('/persons', methods=['POST'])
def post():
    new_person = request.get_json(force=True)
    new_person_id = max([person.id for person in persons]) + 1
    new_person_obj = Person(new_person_id, new_person['name'], new_person['age'], new_person['gender'], new_person['email'])
    persons.append(new_person_obj)
    return jsonify({'PS': 'Post successfull', 'person': new_person_obj.__dict__})

# Define endpoint to update an existing person
@app.route('/persons/<int:person_id>', methods=['PUT'])
def put(person_id):
    updated_person = request.get_json(force=True)
    person = next((p for p in persons if p.id == person_id), None)
    if person:
        person.name = updated_person['name']
        person.age = updated_person['age']
        person.gender = updated_person['gender']
        person.email = updated_person['email']
        return jsonify({'PS': 'Put successfull', 'person': person.__dict__})
    else:
        return jsonify({'error': 'not found'})

# Define endpoint to delete an existing person
@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete(person_id):
    person = next((p for p in persons if p.id == person_id), None)
    if person:
        persons.remove(person)
        return jsonify({'PS': 'Delete successfull'})
    else:
        return jsonify({'error': 'not found'})

class Person:
    def __init__(self, id, name, age, gender, email):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

persons = [
    Person(1, "Alice", 25, "female", "alice.johnson@example.com"),
    Person(2, "Bob", 30, "male", "bob.doe@example.com"),
    Person(3, "Charlie", 35, "female", "charlie.smith@example.com")
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
