from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from apis import models
from apis.db import engine
from fastapi.middleware.cors import CORSMiddleware
from routers import product_route, seller_route, signin

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

# Mount the entire front_end folder as static files
# This makes all your HTML, CSS, JS, images accessible
app.mount("/static", StaticFiles(directory="front_end"), name="static")

# Serve index.html at the root URL
@app.get("/")
async def read_index():
    return FileResponse('front_end/index.html')

# Include your API routers
app.include_router(product_route.router)
app.include_router(seller_route.router)
app.include_router(signin.router)

models.Base.metadata.create_all(engine)





  

