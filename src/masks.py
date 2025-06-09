import re
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "logs" / "mask.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

mask_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_file, mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s: %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
mask_logger.addHandler(file_handler)
mask_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    # Удаляем все символы, кроме цифр
    mask_logger.info("Функция начата")
    card_number = re.sub(r"\D", "", card_number)

    if len(card_number) == 0:
        mask_logger.error("Неверный формат номера карты")
        raise ValueError("Неверный формат номера карты")
    elif len(card_number) < 4:
        mask_logger.error("Неправильное количество цифр")
        return "*" * len(card_number)  # Возвращаем столько звездочек, сколько цифр
    mask_logger.info("Функция завершена успешно")
    return "*" * (len(card_number) - 4) + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    mask_logger.info("Функция начата")
    if not account_number or len(account_number) == 0:
        mask_logger.error("Неверный формат номера счета")
        raise ValueError("Неверный формат номера счета")
    elif len(account_number) < 4:
        mask_logger.error("Неправильное количество цифр")
        return "*" * len(account_number)  # Возвращает одинаковое кол-во * и цифр
    mask_logger.info("Функция завершена успешно")
    return "*" * (len(account_number) - 8) + account_number[-4:]
