from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from logic import Calculation
from pydantic import BaseModel, validator
from datetime import datetime
import json

class MyCustomException(Exception):
    def __init__(self, status_code, msg):
            self.status_code = status_code
            self.msg = msg

class Input(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float

    @validator("date")
    def date_format(cls, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except Exception:
            raise MyCustomException(status_code=400, msg = f"Date format error! Expected date formar dd.mm.yy. Recived: {value}")
        return value

    @validator("periods")
    def val_periods(cls, value):
        if value in range(1,61):
            return value
        else:
            raise MyCustomException(status_code=400, msg = f"Periods format error! Expected periods in range 1-60. Recived: {value}")

    @validator("amount")
    def val_amount(cls, value):
        if value in range(10000,3000001):
            return value
        else:
            raise MyCustomException(status_code=400, msg = f"Amount format error! Expected amount in range 10000,3000001. Recived: {value}")
    
    @validator("rate")
    def val_rate(cls, value):
        if value > 0 and value < 9:
            return value
        else:
            raise MyCustomException(status_code=400, msg = f"Rate format error! Expected rate in range 1,8. Recived: {value}")

app = FastAPI()

@app.exception_handler(MyCustomException)
async def MyCustomExceptionHandler(request: Request, exception: MyCustomException):
    return JSONResponse (status_code = exception.status_code, content = {"error": exception.msg})

@app.post("/predict")
async def predict(request : Input):

    data = json.loads(request.json())

    c = Calculation()
    preds = Calculation.predict_payments(c, json=data)
    
    return preds