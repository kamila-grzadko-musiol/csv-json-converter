from decimal import Decimal
from enum import Enum


class ProductCategory(str, Enum):
    ELECTRONIC = 'Electronic'
    BOOK = 'Book'
    CLOTHING = 'Clothing'


class Product:
    id: int
    name: str
    category: ProductCategory
    price: Decimal



