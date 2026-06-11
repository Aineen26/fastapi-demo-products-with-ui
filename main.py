from fastapi import FastAPI # type: ignore
import database_models
from models import Product
from database import SessionLocal, engine


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hello, World!"}


@app.get("/products")
def get_all_products():
    # db connection
    db = SessionLocal()
    products = db.query(Product).all()
    db.query()
    #query
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
           return product
    return "Product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, updated_product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return  "Product successfully updated"
    return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
        
    return "Product not found"