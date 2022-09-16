# Sber Web Service


### Usage
1. Clone repository.
2. run ```make build```
3. run ```make up```
4. Now you are able to send test data into service: 
```python3 request.py```
5. Test service: ```make test```

### Architecture

[service.py](service.py) launchs an app, validates the input json and call [Calculation](logic.py) class  that does all the math.

Total test coverage 95%.