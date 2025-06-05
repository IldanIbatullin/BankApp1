import re


def get_mask_card_number(card_number: str) -> str:
    # Удаляем все символы, кроме цифр
    card_number = re.sub(r"\D", "", card_number)

    if len(card_number) == 0:
        raise ValueError("Неверный формат номера карты")
    elif len(card_number) < 4:
        return "*" * len(card_number)  # Возвращаем столько звездочек, сколько цифр
    return "*" * (len(card_number) - 4) + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    if not account_number or len(account_number) == 0:
        raise ValueError("Неверный формат номера счета")
    elif len(account_number) < 4:
        return "*" * len(account_number)  # Возвращает одинаковое кол-во * и цифр
    return "*" * (len(account_number) - 8) + account_number[-4:]
