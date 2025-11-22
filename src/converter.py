import csv
import json
from pathlib import Path
from typing import List, Dict


def csv_to_list(csv_path: str) -> List[str]:
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')

        return [row for row in reader]


def save_json(data: List[str], json_path: str) -> None:
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)