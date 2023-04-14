from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = []

@app.route('/add-data', methods=['POST'])
def add_contact():
    if not request.json:
        return jsonify({"status":"error", "message": "Please provide the data"})
    
    contact = {
        'id': contacts[-1]['id'] + 1 if len(contacts) > 0 else 1,
        'name': request.json['name'],
        'contact': request.json['contact'],
        'done': False
    }
    contacts.append(contact)
    return jsonify({"status":"success", "message": "Contact added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

    