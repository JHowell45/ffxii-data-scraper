from dataclasses import dataclass, field
from typing import List
from .base import Accessory
from src.shared import WhereToFind


@dataclass
class Accessories:
    accessories: List[Accessory] = field(default_factory=list)

    def add_accessory(
        self,
        name: str,
        effects: str,
        other_stats: List[str],
        license: str,
        find: WhereToFind,
    ):
        self.accessories.append(
            Accessory(
                name=name,
                effects=effects,
                other_stats=other_stats,
                license=license,
                find=find,
            )
        )

    def serialise(self) -> dict:
        return [accessory.serialise() for accessory in self.accessories]
