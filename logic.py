import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Calculation:

    def __init__(self) -> None:
        pass
    
    def __logic__(self):
        self.predict = {}
        amount = self.data.get("amount")
        periods = self.data.get('periods')
        date = self.data.get('date')
        sum = round(amount * (1 + self.data.get("rate")/12/100), 2)
        for period in range(periods):
            self.predict.update({date: sum})
            date = (datetime.strptime(self.data.get('date'), "%d.%m.%Y") + relativedelta(months=period+1)).strftime('%d.%m.%Y')
            sum = round(sum * (1 + self.data.get("rate")/12/100), 2) 

    def predict_payments(self, json):
        '''
        Function to calculate payments.
        '''
        self.data = json
        self.__logic__()
        return self.predict
