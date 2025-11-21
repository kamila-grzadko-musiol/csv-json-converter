import csv
import json
from pathlib import Path
import logging
from typing import Type, List
from pydantic import BaseModel, ValidationError
from dataclasses import dataclass
from src.model import Product, ProductCategory

logging.basicConfig(level=logging.INFO)


class CsvFileToJsonFileConverter:
    def __init__(self, csv_path: str, model: Type[BaseModel]):
        self.csv_path = Path(csv_path)
        self.model = model
        self.data: List[BaseModel] = []

    def load_csv_data(self):
        logging.info(f'Loading data from CSV file: {self.csv_path}')

        if not self.csv_path.exists():
            logging.error(f'File {self.csv_path} doesnt exist')
            raise FileNotFoundError(f'File not found: {self.csv_path}')

        with open(self.csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            rows = list(reader)

        logging.info(f'Loaded {len(rows)} rows from CSV file')
        return rows



