import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))
labels = {
    0: "versicolor",
    1: "setosa",
    2: "virginica"
}

# API endpoint for prediction
@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    feature = data.get('feature')  # Utilisez get pour éviter des erreurs si 'feature' n'est pas dans les données JSON
    predict = model.predict(feature)
    return jsonify({'prediction': labels[predict[0]]})


# New route for the root path
@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
