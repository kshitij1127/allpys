# calling libraries 
from flask import Flask, jsonify, request

# constructor of the flask - takes name of the current module 
app = Flask(__name__) 
tasks = [  
    {
        'id': 1,
        'title': 'buy groceries',
        'description': 'milk, cheese, fruits, veggies',
        'done': False
    },

    {
        'id': 2,
        'title': 'learn python',
        'description': 'find a good python tutorial on the web',
        'done': False
    },
]

# defining a route
# / is default routing
# by default calls 'get' request of api
# gets called only once  
# post - send data to server to create or update resource 
# put - create and update (only once unlike post)
# delete - delete resources from a server

@app.route("/get-data")
# creating a get method to get all the tasks
def gettasks():
    return jsonify({
        "data": tasks
    })

@app.route("/add-data", methods=["POST"])
def addtasks():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'please provide data'
        }, 400)
    # creating a skeletal structure of how the tasks looks like
    task = {
        'id': tasks[-1]['id'] +1,
        'title': request.json('title'),
        'description': request.json.get('description', ""),
        'done': False,
    }
    tasks.append(task)
    return jsonify({
        "status": 'success',
        "message": 'task added successfully'
    })
if __name__ == '__main__':
    app.run(debug=True)
