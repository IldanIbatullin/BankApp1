# Bank Operations Widget

## Цель проекта
Проект предназначен для обработки банковских операций клиента.

## Установка
1. Клонируйте репозиторий:
```bash
git clone git@github.com:IldanIbatullin/BankApp1.git
```
2. Установите необходимые зависимости (если есть).

## Использование функций

### Функция filter_by_state

```python
filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]

transactions: Список словарей с данными о транзакциях.
state: Статус транзакции для фильтрации (по умолчанию 'EXECUTED').
Пример использования:
python
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]
executed_transactions = filter_by_state(transactions)

Функция sort_by_date
python
sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]

transactions: Список словарей с данными о транзакциях.
descending: Параметр сортировки (по умолчанию — убывание).
Пример использования:
python
sorted_transactions = sort_by_date(transactions)



3. **Сделайте коммит для добавления README-файла**:
```bash
git add README.md
git commit -m "Добавлен README.md с описанием проекта и инструкциями"