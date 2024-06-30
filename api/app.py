#std
from typing import List
#ext
from fastapi import FastAPI, HTTPException, status
#app
from api.schemas.product_schema import CreateProduct, UpdateProduct, GetProduct
from api.repository.product_repository import ProductRepository
from api.database.db_connector import SessionMaker
from api.responses.message import Message


app = FastAPI()

@app.on_event("startup")
async def startup():
    await SessionMaker.create_tables()

@app.get('/', response_model=List[GetProduct])
async def get_product():
    product_repo = ProductRepository(SessionMaker())
    products = await product_repo.find()
    return products


@app.get('/{product_id}', response_model=GetProduct)
async def get_product_by_id(product_id: int):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.find(product_id)
    return product

@app.post('/', response_model=GetProduct)
async def create_product(product: CreateProduct):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.create(product)
    return product

@app.put('/{product_id}', response_model=GetProduct)
async def update_product(product_id: int, updated_product: UpdateProduct):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.find(product_id)
    if not isinstance(product, list):
        product = await product_repo.update(product, updated_product)
        return product
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="The given id is invalid"
    )

@app.delete('/{product_id}', response_model=Message)
async def delete_product(product_id: int):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.find(product_id)
    if not isinstance(product, list):
        reponse = await product_repo.delete(product)
        return reponse
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="The given id is invalid"
    )
