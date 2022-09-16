import requests

data = {
    "date": "31.01.2021",
    "periods": 3,
    "amount": 10000,
    "rate": 8
}

res = requests.post('http://0.0.0.0:8000/predict', json=data)

print(res)
print(res.json())