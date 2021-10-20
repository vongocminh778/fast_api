from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Set
import requests
import json


app = FastAPI()

class Sender(BaseModel):
    id: str

class Recipient(BaseModel):
    id: str

class Message(BaseModel):
    msg_id: str
    text: str

class Item(BaseModel):
    app_id: Optional[str] = None
    user_id_by_app: Optional[str] = None
    event_name: Optional[str] = None
    timestamp: Optional[str] = None
    sender: Optional[Sender] = None
    recipient: Optional[Recipient] = None
    message: Optional[Message] = None

@app.get('/test')
async def test():
    x = requests.get('https://oauth.zaloapp.com/v4/oa/permission?app_id=1960458872042889409&redirect_uri=https%3A%2F%2Fmrd-mic.herokuapp.com%2Ftest&code_challenge=f0EMbmD-7QACgIeZeAdPFEyxRa3kfqyn25N2nDTAg0E')
    print(x.status_code)
    # return "success fastapi"
    return x.json()

@app.post('/')
async def test(item:Item):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = json.loads(item.json())
    response = requests.post("http://113.161.152.35:2090/api/Maintenance/getzalo", json=res, headers=headers)
    return response.text
