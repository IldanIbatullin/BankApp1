import pytest
from src.processing import (filter_by_state, sort_by_date)

# Пример данных для тестов
transactions = [
    {"date": "2024-12-01", "state": "EXECUTED"},
    {"date": "2024-11-30", "state": "PENDING"},
    {"date": "2024-12-02", "state": "EXECUTED"},
    {"date": "2024-11-29", "state": "EXECUTED"},
]


# Фикстура для тестов
@pytest.fixture
def sample_transactions():
    return transactions


# Тесты для filter_by_state
def test_filter_by_state(sample_transactions):
    executed_transactions = filter_by_state(sample_transactions, 'EXECUTED')
    assert len(executed_transactions) == 3
    assert all(tx['state'] == 'EXECUTED' for tx in executed_transactions)


# Тесты для sort_by_date
def test_sort_by_date(sample_transactions):
    sorted_transactions = sort_by_date(sample_transactions)
    assert sorted_transactions[0]['date'] == '2024-12-02'
    assert sorted_transactions[-1]['date'] == '2024-11-29'




