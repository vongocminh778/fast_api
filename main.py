from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
async def test():
    return "success fastapi"