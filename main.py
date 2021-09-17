from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
async def test():
    return "success fastapi"

@app.get('/', status_code=200)
async def test():
    return ""