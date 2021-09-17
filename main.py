from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
async def test():
    return "success fastapi"

@app.post('/', status_code=200)
async def test():
    return ""