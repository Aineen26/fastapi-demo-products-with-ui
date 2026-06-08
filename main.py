from fastapi import FastAPI # type: ignore
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello, World!"}

products = [
    Product(id=1, name="Laptop", description="High-performance laptop", price=999.0, quantity=10),
    Product(id=2, name="Smartphone", description="Latest model smartphone", price=499.0, quantity=20),
    Product(id=3, name="Tablet", description="Portable tablet", price=299.0, quantity=15)
]

@app.get("/products")
def get_all_products():
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