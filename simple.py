import sys
from fastapi import FastAPI
print(sys.version)

app = FastAPI()
@app.get("/")
async def HelloWorld():
    return {"message": "Hello World"}