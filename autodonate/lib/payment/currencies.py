"""File represents IDs in database for all supported currencies."""
from enum import Enum


class Currency(Enum):
    RUB = 0
    UAH = 1
    USD = 2
    EUR = 3
