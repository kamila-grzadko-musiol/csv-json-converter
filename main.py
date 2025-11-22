from src.converter import csv_to_list, save_json
from src.model import Product


def main() -> None:
    products = csv_to_list("data_csv/example.csv")
    save_json(products, 'data_json/example.json')


if __name__ == '__main__':
    main()
