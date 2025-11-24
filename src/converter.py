import csv
import json
from pathlib import Path
from typing import List, Dict
from src.model import Product, ProductCategory
from decimal import Decimal


def csv_to_products(csv_path: str) -> List[Product]:
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    products: List[Product] = []

    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            product = Product(
                id=int(row["id"]),
                name=row["name"],
                category=ProductCategory(row["category"]),
                price=Decimal(row["price"])
            )
            products.append(product)
        return products


def save_json(data: List[str], json_path: str) -> None:
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)