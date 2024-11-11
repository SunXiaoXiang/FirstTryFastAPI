import sys
from fastapi import FastAPI
print(sys.version)

app = FastAPI()
@app.get("/")
async def HelloWorld():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
    async def read_item(item_id: int):
    return {"item_id": item_id}