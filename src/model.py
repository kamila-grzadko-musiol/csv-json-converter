from pydantic import BaseModel, Field
from decimal import Decimal
from enum import Enum
from typing import TypedDict


class ProductCategory(Enum):
    ELECTRONIC = 'Electronic'
    BOOK = 'Book'
    CLOTHING = 'Clothing'


class ProductDataDict(TypedDict):
    id: int
    name: str
    category: str
    price: str


class Product(BaseModel):
    id: int = Field(..., ge=1)
    name: str
    category: ProductCategory
    price: Decimal = Field(..., ge=0)

    def to_dict(self) -> ProductDataDict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "price": str(self.price)
        }



