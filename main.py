from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI()

class User(BaseModel):
    date: datetime
    message: str
        
@app.post('ping')
def ping(body: User):
    pass

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)
