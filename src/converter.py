import csv
import json
import logging
from pathlib import Path
from src.model import Product, ProductCategory
from decimal import Decimal


logging.basicConfig(level=logging.INFO)


class CsvToJsonConverter:

    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self.products: list[Product] = []

    def csv_to_products(self) -> list[Product]:

        if not self.csv_path.exists():
            logging.error(f"CSV file not found: {self.csv_path}", )
            raise FileNotFoundError(f"File not found: {self.csv_path}")

        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=';')

            for row in reader:
                product = Product(
                    id=int(row["id"]),
                    name=row["name"],
                    category=ProductCategory(row["category"]),
                    price=Decimal(row["price"])
                )
                self.products.append(product)
            return self.products

    def save_json(self, json_path: str) -> None:
        json_data = [row.to_dict() for row in self.products]

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

    def _convert(self, json_path: str) -> None:
        self.csv_to_products()
        self.save_json(json_path)
