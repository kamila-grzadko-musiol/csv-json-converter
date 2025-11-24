from decimal import Decimal
from enum import Enum


class ProductCategory(str, Enum):
    ELECTRONIC = 'Electronic'
    BOOK = 'Book'
    CLOTHING = 'Clothing'


class Product:
    def __init__(self, id: int, name: str, category: ProductCategory, price: Decimal):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "price": str(self.price)
        }



