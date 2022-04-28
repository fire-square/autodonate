"""Package containing all api dataclasses."""

from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Player:
    """Player dataclass."""

    nick: str


@dataclass_json
@dataclass
class Donation:
    """Donation dataclass."""

    id: int
    name: str
    price: float
    player: Player


@dataclass_json
@dataclass
class LatestDonates:
    """Last donations dataclass."""

    donates: List[Donation]
