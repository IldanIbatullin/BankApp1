import os.path

import pytest
from src.utils import load_json_file
import json

def test_load_json_file(transactions_from_to):
    """работа функцмм"""
    try:
        with open("test.json","w",encoding="utf-8") as file:
            json.dump(transactions_from_to,file,indent=4,ensure_ascii=False)

        assert load_json_file("test.json") == transactions_from_to
    finally:
        if os.path.exists("test.json"):
            os.remove("test.json")


def test_load_json_file_non_existent_file():
    """тест если файл не найден"""
    assert load_json_file("non.json") == []


def test_load_json_file_invalid_json():
    """Файл с неккоректными данными"""
    try:
        with open("test.json","w",encoding="utf-8") as file:
            file.write("Error")

        assert load_json_file("test.json") == []
    finally:
        if os.path.exists("test.json"):
            os.remove("test.json")
