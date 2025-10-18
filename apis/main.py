from fastapi import FastAPI
from apis import models
from apis.db import engine
from fastapi.middleware.cors import CORSMiddleware
from . routers import product_route, seller_route, signin
from fastapi.responses import HTMLResponse


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





@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
    <head><title>Product Management System</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>🚀 Product Management System</h1>
        <p>Welcome to the Product Management API</p>
        <a href="/docs" style="padding: 10px 20px; background: blue; color: white; text-decoration: none; border-radius: 5px;">View API Documentation</a>
    </body>
    </html>
    """


app.include_router(product_route.router)

app.include_router(seller_route.router)

app.include_router(signin.router)

models.Base.metadata.create_all(engine)







  

