import pytest
from src.model import ProductDataDict, Product
from src.converter import CsvToJsonConverter
from pathlib import Path
import json
from pytest import FixtureRequest


def test_converter_matches_expected_json(converter, tmp_path: Path, products_file) -> None:
    output_json = tmp_path / "expected_products.json"

    converter._convert(str(output_json))

    with open(output_json, "r", encoding="utf-8") as f:
        result_data = json.load(f)

    with open(products_file, "r", encoding="utf-8") as f:
        expected_data = json.load(f)

    assert result_data == expected_data

