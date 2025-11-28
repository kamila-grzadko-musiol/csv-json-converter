import pytest
from src.model import Product, ProductCategory, ProductDataDict
from src.converter import CsvToJsonConverter
from decimal import Decimal
from pathlib import Path
import json


@pytest.fixture
def product_1() -> Product:
    return Product(id=101, name="Laptop", category=ProductCategory.ELECTRONIC, price=Decimal("1500.00"))


@pytest.fixture
def product_1_data() -> ProductDataDict:
    return {"id": 101, "name": "Laptop", "category": "Electronic", "price": "1500.00"}


@pytest.fixture
def product_2() -> Product:
    return Product(id=102, name="T-Shirt", category=ProductCategory.CLOTHING, price=Decimal("20.00"))


@pytest.fixture
def product_2_data() -> ProductDataDict:
    return {"id": 102, "name": "T-Shirt", "category": "Clothing", "price": "20.00"}


@pytest.fixture
def products_data(product_1_data: ProductDataDict, product_2_data: ProductDataDict) -> list[ProductDataDict]:
    return [product_1_data, product_2_data]

CSV_DATA = """id;name;category;price
1;Laptop;Electronic;1999.99
2;Book title;Book;29.90
"""

@pytest.fixture
def csv_file(tmp_path: Path):
    """Create a temporary CSV file for tests."""
    file = tmp_path / "products.csv"
    file.write_text(CSV_DATA, encoding="utf-8")
    return file

@pytest.fixture
def converter(csv_file: Path):
    """Provide converter instance ready for use."""
    return CsvToJsonConverter(str(csv_file))

@pytest.fixture
def products_file(tmp_path: Path, products_data: list[ProductDataDict]) -> str:
    json_path = tmp_path / "expected_products.json"
    json_path.write_text(json.dumps(products_data, indent=4), encoding="utf-8")
    return str(json_path)
