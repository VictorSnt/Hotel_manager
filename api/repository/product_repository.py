#std
from typing import Dict, List, Optional, Union
#ext
from fastapi import HTTPException
from sqlmodel import select
#app
from api.database.db_connector import SessionMaker
from api.model.product import Product
from api.schemas.product_schema import CreateProduct, UpdateProduct


class ProductRepository:
    """
        Find products by ID or return all products if no ID is provided.

        Args:
            prod_id (Optional[int]): ID of the product to find.

        Returns:
            Union[Product, List[Product]]: A single product if ID is provided,
            a list of products otherwise.

        Raises:
            HTTPException: If no product(s) are found.
    """

    def __init__(self, session_maker: SessionMaker) -> None:
        self.session_maker = session_maker

    async def find(self, prod_id: Optional[int] = None) -> Union[Product, List[Product]]:
        async with self.session_maker.get_session_async() as session:
            if prod_id:
                statement = select(Product).where(
                    (Product.id == prod_id) & (Product.active == True)
                )
                result = await session.exec(statement)
                response = result.one_or_none()
            else:
                statement = select(Product).where(Product.active == True)
                result = await session.exec(statement)
                response = list(result.all())

            if not response:
                raise HTTPException(status_code=404, detail="None product found")
            return response

    async def create(self, created_product: CreateProduct) -> Product:
        new_product = Product(**created_product.model_dump())
        async with self.session_maker.get_session_async() as session:
            session.add(new_product)
            await session.commit()
            await session.refresh(new_product)
            return new_product

    async def update(self, product: Product, updated_product: UpdateProduct) -> Product:
        async with self.session_maker.get_session_async() as session:
            product_data = updated_product.model_dump(exclude_unset=True)
            for key, value in product_data.items():
                setattr(product, key, value)
            session.add(product)
            await session.commit()
            await session.refresh(product)
            return product

    async def delete(self, product: Product) -> Dict:
        async with self.session_maker.get_session_async() as session:
            setattr(product, 'active', False)
            session.add(product)
            await session.commit()
            await session.refresh(product)
            return {"detail": "Product deleted successfully"}
