from flask import Flask, request, jsonify

app = Flask(__name__)
contacts = [
    {
        'id': 1,
        'name': 'Virat',
        'contact': '1202303403',
        'done': False
    }, 

    {
        'id': 2,
        'name': 'Dhoni',
        'contact': '1212121212',
        'done': False,
    }
]

@app.route('/get-data')
def gettasks():
    return jsonify({
        "data": contacts
    })

@app.route("/add-data", methods=["POST"])
def addcontacts():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'please provid data to add'
        }, 400)
    contact = {
        'id': contacts[-1]['id'] + 1,
        'title': request.json('title'),
        'description': request.json.get('description', ""),
        'done': False,
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "new contacţ added successfully"
    })

if __name__ == '__main__':
    app.run()