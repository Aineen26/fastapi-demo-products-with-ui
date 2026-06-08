from pydantic import BaseModel  # type: ignore
 # type: ignore[reportMissingImports]
class Product(BaseModel):
        id: int
        name: str
        description: str
        price: float
        quantity: int

   
