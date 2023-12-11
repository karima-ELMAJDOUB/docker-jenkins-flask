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

## Nouvelle route pour la racine
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Code de prédiction pour la méthode POST
            data = request.get_json(force=True)
            feature = data.get('feature')
            
            print(f"Received feature for prediction: {feature}")
            
            predict = model.predict(feature)
            
            print(f"Prediction result: {predict}")
            
            prediction_label = labels[predict[0]]
            
            print(f"Prediction label: {prediction_label}")
            
            return jsonify({'prediction': prediction_label})
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return jsonify({'error': 'An error occurred during prediction.'})
    else:
        # Code pour la méthode GET
        return 'This is a GET request. Use POST request with data for predictions.'


# New route for the root path
#@app.route('/')
#def home():
# return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
