"""File represents IDs in database for all supported currencies."""
from enum import Enum, unique


@unique
class Currency(Enum):
    """Object represents IDs in database for all supported currencies.

    Examples:
        >>> print(Currency.RUB.name)
        RUB
        >>> print(Currency.UAH.value)
        1

        Also, you can use `for` loop with this class.
    """

    #: Russian Ruble.
    RUB = 0
    #: Ukrainian Hryvnia.
    UAH = 1
    #: American Dollar.
    USD = 2
    #: Euro.
    EUR = 3
