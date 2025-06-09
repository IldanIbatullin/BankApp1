import json
import logging
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "logs" / "utils.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(log_file, mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s: %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def load_json_file(file_path):
    """
    Загружает данные из JSON-файла.

    :param file_path: Путь к файлу.
    :return: Содержимое файла как словарь, или пустой список в случае ошибки.
    """
    utils_logger.info("Функция начата")

    try:
        utils_logger.info("Начато преобразование Json файла в обьект Python")
        with open(file_path, "r", encoding="utf-8") as file:
            result = json.load(file)
            utils_logger.info("Преобразование успешно выполнено")
            return result
    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}. Возвращаем пустой список.")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле: {file_path}. Возвращаем пустой список.")
        return []
