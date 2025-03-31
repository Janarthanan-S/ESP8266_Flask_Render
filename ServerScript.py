from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []  # Simple in-memory storage

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Expecting JSON data
    if not data:
        return jsonify({'error': 'No data received'}), 400
    
    data_store.append(data)  # Store the data
    print(f"Received data: {data}")  # Print received data to Flask terminal
    return jsonify({'message': 'Data stored successfully'}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'stored_data': data_store}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
