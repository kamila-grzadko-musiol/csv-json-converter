from pydantic import BaseModel, Field
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class ProductCategory(Enum):
    ELECTRONIC = 'Electronic'
    BOOK = 'Book'
    CLOTHING = 'Clothing'


@dataclass
class Product(BaseModel):
    id: int
    name: str
    category: ProductCategory
    price: Decimal = Field(..., gt=0, description="The price must be greater than zero")



