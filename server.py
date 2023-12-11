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

# Modifier la route /api pour accepter également la méthode GET
@app.route('/api', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Code de prédiction pour la méthode POST
        data = request.get_json(force=True)
        feature = data.get('feature')
        predict = model.predict(feature)
        return jsonify({'prediction': labels[predict[0]]})
    else:
        # Code pour la méthode GET
        return 'non prediction !'

# New route for the root path
#@app.route('/')
#def home():
# return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
