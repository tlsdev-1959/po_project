from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get('/get/budget', name='get budget')
async def getBudget(request: Request):
    return {'budget': 0}

if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=9343, reload=True)