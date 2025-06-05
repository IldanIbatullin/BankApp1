from datetime import datetime

# src/widget.py


def mask_account_card(account_type: str) -> str:
    if account_type not in ["card", "account"]:
        raise ValueError("Неверный тип аккаунта")
    return f"masked_{account_type}"


# src/widget.py
def get_date(date_string: str) -> str:
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        return None
