from fastapi import FastAPI
from apis import models
from apis.db import engine
from fastapi.middleware.cors import CORSMiddleware
from . routers import product_route, seller_route, signin



app = FastAPI(
  title="Products",
  description="Find details for the products",
  
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.include_router(product_route.router)

app.include_router(seller_route.router)

app.include_router(signin.router)

models.Base.metadata.create_all(engine)







  

