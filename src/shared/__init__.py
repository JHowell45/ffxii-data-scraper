from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class WhereToFind:
    purchased: List[str] = field(default_factory=list)
    bazaar: List[str] = field(default_factory=list)
    stolen: List[str] = field(default_factory=list)
    treasure: List[str] = field(default_factory=list)
    side_quest: List[str] = field(default_factory=list)
    poached: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, List[str]]):
        return cls(
            purchased=data.get("purchased", []),
            bazaar=data.get("bazaar", []),
            stolen=data.get("stolen", []),
            treasure=data.get("treasure", []),
            side_quest=data.get("side_quest", []),
            poached=data.get("poached", []),
        )

    def add_purchased(self, purchase: str):
        self.purchased.append(purchase)

    def add_treasure(self, treasure: str):
        self.treasure.append(treasure)

    def serialise(self) -> dict:
        return {
            "purchased": self.purchased,
            "bazaar": self.bazaar,
            "stolen": self.stolen,
            "treasure": self.treasure,
            "side_quest": self.side_quest,
            "poached": self.poached,
        }
