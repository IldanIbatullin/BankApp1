import pytest
from src.masks import (get_mask_card_number, get_mask_account)
# Параметризованные тесты для get_mask_card_number
@pytest.mark.parametrize("input_card, expected_output", [
    ("1234567812345678", "************5678"),
    ("1234-5678-1234-5678", "************5678"),
    ("12345", "*2345"),
    ("12", "**"),      # Добавлено для проверки короткого номера
    ("", ""),          # Проверка пустой строки
])
def test_get_mask_card_number(input_card, expected_output):
    if input_card == "":
        with pytest.raises(ValueError):
            get_mask_card_number(input_card)
    else:
        assert get_mask_card_number(input_card) == expected_output

@pytest.mark.parametrize("input_account, expected_output", [
    ("12345678901234567890", "************7890"),
    ("123", "***"),
    ("12", "**"),      # Добавлено для проверки короткого номера
])
def test_get_mask_account(input_account, expected_output):
    if input_account == "":
        with pytest.raises(ValueError):
            get_mask_account(input_account)
    else:
        assert get_mask_account(input_account) == expected_output