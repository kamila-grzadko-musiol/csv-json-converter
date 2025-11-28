from src.model import Product, ProductDataDict


def test_product_to_dict(product_1: Product, product_1_data: ProductDataDict) -> None:
    data = product_1.to_dict()
    assert data == product_1_data
