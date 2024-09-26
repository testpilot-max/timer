from fastapi import FastAPI, HTTPException
from typing import List, Dict
import random
from datetime import datetime, timedelta

app = FastAPI()

userDatabase = {}

@app.post('/user_stats')
async def calculate_user_statistics(user_data:Dict[str,List[float]]):
    user_id=random.randint(1000,9999)
    userDatabase[user_id]=user_data
    
    def calculate_average(numbers):
        return sum(numbers)/len(numbers)
    
    def calcMedian( numbers ):
        sorted_numbers = sorted(numbers)
        length = len(sorted_numbers)
        if length % 2 == 0:
            return (sorted_numbers[length//2 - 1] + sorted_numbers[length//2]) / 2
        else:
            return sorted_numbers[length//2]
    
    results={}
    for metric,values in user_data.items():
        avg=calculate_average(values)
        median=calcMedian(values)
        results[metric]={'average':avg,'median':median}
    
    last_update_time=datetime.now()
    next_update=last_update_time+timedelta(hours = 24)
    
    response = {
        'user_id':user_id,
        'statistics':results,
        'last_updated':last_update_time.strftime('%Y-%m-%d %H:%M:%S'),
        'next_update':next_update.strftime('%Y-%m-%d %H:%M:%S'),
        'data_points':sum([len(v) for v in user_data.values()]),
    }
    
    return response

@app.get('/get_user_stats/{user_id}')
async def get_user_statistics(user_id: int):
    if user_id not in userDatabase:
        raise HTTPException(status_code=404,detail='User not found')
    return {'user_id':user_id,'data':userDatabase[user_id]}
