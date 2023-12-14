import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# Load the model
model = pickle.load(open('model.pkl', 'rb'))
labels = {
    0: "versicolor",
    1: "setosa",
    2: "virginica"
}

# Fonction de prédiction
def predict_default():
    # Utilisez des valeurs par défaut pour la prédiction
    default_feature = [[1.8, 1.0, 2.2, 3.2]]
    prediction = model.predict(default_feature)
    return labels[prediction[0]]

# Route pour la racine
@app.route('/')
def home():
    # Appel de la fonction de prédiction par défaut
    prediction_result = predict_default()
    return render_template('result.html', prediction_result=prediction_result)

# Route pour l'API de prédiction
@app.route('/api', methods=['POST'])
def predict():
    # Code de prédiction pour la méthode POST
    data = request.get_json(force=True)
    feature = data.get('feature')
    predict = model.predict(feature)
    return jsonify({'prediction': labels[predict[0]]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
