from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
async def test():
    return "success fastapi"

@app.post('/')
async def test():
    return "200 OK"