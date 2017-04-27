from flask import Flask, jsonify, request, render_template #import flask
#json always uses double quptes and never single quotes

app = Flask(__name__) #create object of Flask using a unique name

# POST - used to receive data (we are the server)
# GET - used to send data back only

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
            'name': 'My Item',
            'price': 15.99
            }
        ]

    }

]

@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)
    #have to return a string

#GET /store/<string:name>
@app.route('/store/<string:name>') #'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    #iterate over stores
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    #if the store name matches, retunrn it
    #if none match, return an error message

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
#POST /store/<string:name>/item {name:, price: }

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
    return jsonify({'message:' 'store not found'})
    #have to return a string


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)
