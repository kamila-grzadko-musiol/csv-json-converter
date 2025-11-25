from src.converter import CsvToJsonConverter


def main() -> None:
    conv = CsvToJsonConverter("data_csv/example.csv")
    products = conv.csv_to_products()
    print(products)
    conv.save_json("data_json/example.json")


if __name__ == '__main__':
    main()
