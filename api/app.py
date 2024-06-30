#ext
from fastapi import FastAPI
#app
from api.database.db_connector import SessionMaker
from api.routes.product_router import product_router
from api.routes.room_router import room_router


app = FastAPI()
@app.on_event("startup")
async def startup():
    await SessionMaker.create_tables()

app.include_router(product_router)
app.include_router(room_router)
