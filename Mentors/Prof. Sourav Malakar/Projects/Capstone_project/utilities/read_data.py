import csv
import configparser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def read_config(section, key):
    config = configparser.ConfigParser()
    config_path = BASE_DIR / "config" / "config.ini"
    config.read(config_path)
    return config.get(section, key)

def read_csv_data(filename):
    file_path = BASE_DIR / "test_data" / filename
    rows = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows