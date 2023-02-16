from dataclasses import dataclass, field
from typing import List
from .base import Accessory


@dataclass
class Accessories:
    accessories: List[Accessory] = field(default_factory=list)

    def serialise(self) -> dict:
        return [accessory.serialise() for accessory in self.accessories]
