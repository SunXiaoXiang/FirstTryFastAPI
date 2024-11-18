from fastapi import Body, FastAPI
from typing import Annotated

app = FastAPI()


@app.put("/items/")
async def read_item(item_id: Annotated[int, Body()]):
    return {"item_id": item_id}