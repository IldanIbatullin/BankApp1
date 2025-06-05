import pytest
from src.widget import (mask_account_card, get_date)
# Тесты для mask_account_card (пример)
def test_mask_account_card():
    # Пример теста для mask_account_card (необходимо адаптировать под вашу реализацию)
    assert mask_account_card("card") == "masked_card"


# Тесты для get_data (пример)
def test_get_data():
    assert get_date("2024-12-08") == "08/12/2024"