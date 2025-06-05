from typing import List, Dict


def filter_by_state(
    transactions: List[Dict[str, str]], state: str = "EXECUTED"
) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Значение состояния для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те, которые соответствуют указанному состоянию.
    """
    return [
        transaction for transaction in transactions if transaction.get("state") == state
    ]


def sort_by_date(
    transactions: List[Dict[str, str]], reverse: bool = True
) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей с данными о банковских операциях.
    :param reverse: Порядок сортировки (по умолчанию True — убывание).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
