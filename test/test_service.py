from fastapi.testclient import TestClient
import sys
sys.path.append(".")
from service import app
import json

client = TestClient(app)

def test_200():
    with open('test/test_cases/valid.json') as f:
        data  = json.loads(f.read())    
    res = client.post('http://127.0.0.1:8000/predict', json=data)
    assert str(res) == '<Response [200]>'

def test_invalid_date():
    with open('test/test_cases/invalid_date.json') as f:
        data  = json.loads(f.read())  
    res = client.post('http://127.0.0.1:8000/predict', json=data)
    assert str(res) == '<Response [400]>'

def test_invalid_periods():
    with open('test/test_cases/invalid_periods.json') as f:
        data  = json.loads(f.read())  
    res = client.post('http://127.0.0.1:8000/predict', json=data)
    assert str(res) == '<Response [400]>'

def test_invalid_amount():
    with open('test/test_cases/invalid_amount.json') as f:
        data  = json.loads(f.read())  
    res = client.post('http://127.0.0.1:8000/predict', json=data)
    assert str(res) == '<Response [400]>'

def test_invalid_rate():
    with open('test/test_cases/invaild_rate.json') as f:
        data  = json.loads(f.read())  
    res = client.post('http://127.0.0.1:8000/predict', json=data)
    assert str(res) == '<Response [400]>'

def test_invalid_endpoint():
    with open('test/test_cases/valid.json') as f:
        data  = json.loads(f.read())
    res = client.post('http://127.0.0.1:8000/invalid', json=data)
    assert str(res) == '<Response [404]>'   

def test_ligic():
    with open('test/test_cases/valid.json') as f:
        data  = json.loads(f.read())    
    res = client.post('http://127.0.0.1:8000/predict', json=data)
    assert str(res.json()) == '{\'status\': \'SUCCESS\', \'data\': {\'31.01.2021\': 10050.0, \'28.02.2021\': 10100.25, \'31.03.2021\': 10150.75}}'