from enum import Enum


class CarAdRegex(Enum):
    PRICE = (
        r"^\d+(\.\d{1,2})? (UAH|USD|EUR)$",
        "Acceptable input options: 10 UAH or 100 USD or 100.50 EUR"
    )