from typing import Dict
from api.model.product import Product
from api.repository.base_repository import BaseRepository
from api.schemas.product_schema import CreateProduct
from api.database.db_connector import SessionMaker


class ProductRepository(BaseRepository):
    """
    Repository class for handling operations related to Product entities.
    """

    def __init__(self, session_maker: SessionMaker):
        super().__init__(session_maker, Product)

    async def create(self, created_product: CreateProduct) -> Product:
        new_product = Product(**created_product.model_dump())
        return await super().create(new_product)

    async def find_and_update(self, product: Product) -> Product:
        return await super().find_and_update(product, {}, lambda x: x)

    async def find_and_delete(self, product: Product) -> Dict:
        return await super().find_and_delete(product)
