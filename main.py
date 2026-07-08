from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = [
    {
        "id": 101,
        "name": "Wireless Mouse",
        "price": 500,
        "quantity": 10
    },
    {
        "id": 102,
        "name": "Mechanical Keyboard",
        "price": 1800,
        "quantity": 7
    },
    {
        "id": 103,
        "name": "USB-C Charger",
        "price": 900,
        "quantity": 15
    },
    {
        "id": 104,
        "name": "Bluetooth Speaker",
        "price": 2200,
        "quantity": 5
    },
    {
        "id": 105,
        "name": "Laptop Stand",
        "price": 1200,
        "quantity": 12
    }
]


class ProductUpdate(BaseModel):
    name: str
    price: int
    quantity: int


@app.get('/products')
def get_products():
    return products


@app.put('/products/{product_id}')
def update_product(product_id: int, product: ProductUpdate):
    for exisiting_product in products:
        if exisiting_product["id"] == product_id:
            exisiting_product["name"] = product.name
            exisiting_product["price"] = product.price
            exisiting_product["quantity"] = product.quantity
            return {
                "message": "Product updated succesfully",
                "product": exisiting_product
            }
    raise HTTPException(status_code=404, detail="Product Not Found")
