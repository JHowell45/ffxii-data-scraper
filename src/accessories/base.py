from dataclasses import dataclass, field
from typing import List
from src.shared import WhereToFind


@dataclass
class Accessory:
    effects: str
    other_stats: List[str]
    license: str
    find: WhereToFind
