from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    date: datetime
    message: str
        
@app.webhooks.post('ping')
def ping(body: User):
    pass