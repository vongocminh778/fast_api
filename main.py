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
    return "success fastapi"

_json = {"app_id": "1960458872042889409","user_id_by_app": "5224557294600520762","event_name": "user_send_text","timestamp": "1631857569625","sender": {"id": "4574232636154508063"},"recipient": {"id": "579745863508352884"},"message": {"msg_id": "This is message id","text": "This is testing message"}}
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
@app.post('/')
async def test(item:Item):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post("http://113.161.152.35:2090/api/Maintenance/getzalo", json=_json, headers=headers)
    # print(response.content,response.text, response.headers, response.status_code,response.reason)
    return response.text
