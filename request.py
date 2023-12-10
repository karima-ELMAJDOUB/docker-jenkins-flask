import requests

# Change the value of feature that you want to test
url = 'http://127.0.0.1:5000/api'
feature = {'feature': [[5.8, 4.0, 1.2, 5.2]]}

r = requests.post(url, json=feature)
print(r.json())
