import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Define the base URL of your Express API
    express_api_base_url = 'http://localhost:3000/'

    # Construct the full URL by appending the requested path
    full_url = express_api_base_url + path

    # Forward the request to the Express API
    if request.method == 'GET':
        response = requests.get(full_url)
    elif request.method == 'POST':
        response = requests.post(full_url, json=request.json)
    elif request.method == 'PUT':
        response = requests.put(full_url, json=request.json)
    elif request.method == 'DELETE':
        response = requests.delete(full_url)

    # Return the response from the Express API to the client
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(port=5009)

