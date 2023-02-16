from dataclasses import dataclass, field
from typing import List
from src.shared import WhereToFind


@dataclass
class Accessory:
    name: str
    effects: str
    other_stats: List[str]
    license: str
    find: WhereToFind

    def serialise(self) -> dict:
        return {
            "name": self.name,
            "effects": self.effects,
            "other_stats": self.other_stats,
            "license": self.license,
            "find": self.find.serialise(),
        }
