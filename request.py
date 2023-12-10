import requests

# Change the value of features that you want to test
url = 'http://127.0.0.1:5000/api'
features = [[5.8, 4.0, 1.2, 5.2]]

# Send a POST request with the features
r = requests.post(url, json={'feature': features})

# Print the prediction result
print(r.text)
