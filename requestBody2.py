from fastapi import FastAPI
app = FastAPI()
@app.put("/items/")
async def read_item(item_id: int, name: str):
    return {"item_id": item_id, "name": name}