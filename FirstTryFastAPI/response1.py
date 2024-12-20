from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from loguru import logger

app = FastAPI()

# 配置loguru
logger.add(
    "logs/app.log",
    rotation="1 MB",
    retention="7 days",
    level="INFO",
    backtrace=True,
    diagnose=True,
)


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    logger.debug(f"创建用户为:{user}")
    return user


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    if item_id not in items:
        logger.error("item_id 不存在")
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
