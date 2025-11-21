from src.converter import CsvFileToJsonFileConverter
from src.model import Product


def main() -> None:
    converter = CsvFileToJsonFileConverter("data_csv/example.csv", Product)
    print(converter.load_csv_data())


if __name__ == '__main__':
    main()
