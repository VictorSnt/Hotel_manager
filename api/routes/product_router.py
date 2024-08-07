#std
from typing import List
#ext
from fastapi import APIRouter
#app
from api.schemas.product_schema import CreateProduct, UpdateProduct, GetProduct
from api.repository.product_repository import ProductRepository
from api.database.db_connector import SessionMaker
from api.responses.message import Message


product_router = APIRouter(prefix='/product')
@product_router.get('/', response_model=List[GetProduct])
async def get_product():
    product_repo = ProductRepository(SessionMaker())
    products = await product_repo.find()
    return products


@product_router.get('/{product_id}', response_model=GetProduct)
async def get_product_by_id(product_id: int):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.find(product_id)
    return product

@product_router.post('/', response_model=GetProduct)
async def create_product(product: CreateProduct):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.create(product.model_dump())
    return product

@product_router.put('/{product_id}', response_model=GetProduct)
async def find_and_update_product(product_id: int, updated_product: UpdateProduct):
    product_repo = ProductRepository(SessionMaker())
    product = await product_repo.find_and_update(product_id, updated_product)
    return product

@product_router.delete('/{product_id}', response_model=Message)
async def find_and_delete_product(product_id: int):
    product_repo = ProductRepository(SessionMaker())
    reponse = await product_repo.find_and_delete(product_id)
    return reponse
