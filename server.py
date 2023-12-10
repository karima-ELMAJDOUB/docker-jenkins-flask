from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))
labels = {
    0: "versicolor",
    1: "setosa",
    2: "virginica"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the features from the form
    feature = [float(request.form['sepal_length']),
               float(request.form['sepal_width']),
               float(request.form['petal_length']),
               float(request.form['petal_width'])]
    
    # Make a prediction
    prediction = model.predict([feature])[0]
    predicted_label = labels[prediction]

    return render_template('index.html', prediction=predicted_label)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

