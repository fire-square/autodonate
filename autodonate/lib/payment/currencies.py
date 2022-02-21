"""File represents IDs in database for all supported currencies."""
from enum import Enum


class Currency(Enum):
    """Object represents IDs in database for all supported currencies.

    Examples:
        >>> print(Currency.RUB.name)
        RUB
        >>> print(Currency.UAH.value)
        1

        Also, you can use `for` loop with this class.

    Attributes:
        RUB: Russian Ruble.
        UAH: Ukranian Hryvnia.
        USD: American Dollar.
        EUR: Euro.
    """

    RUB = 0
    UAH = 1
    USD = 2
    EUR = 3
