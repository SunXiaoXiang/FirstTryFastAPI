from fastapi import FastAPI
app = FastAPI()
@app.put("/items/")
async def read_item(item_id: int):
    return {"item_id": item_id}