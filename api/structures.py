"""Package containing all api dataclasses"""

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List, Dict


@dataclass_json
@dataclass
class Player:
    nick: str


@dataclass_json
@dataclass
class Donation:
    id: int
    name: str
    price: float
    player: Player


@dataclass_json
@dataclass
class LatestDonates:
    donates: List[Donation]
