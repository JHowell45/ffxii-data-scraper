from dataclasses import dataclass, field
from typing import List
from enum import Enum


class MagickType(Enum):
    ARCANE: 1
    BLACK: 2
    GREEN: 3
    TIME: 4
    WHITE: 5


@dataclass
class WhereToFind:
    purchased: List[str] = field(default_factory=list)
    treasure: List[str] = field(default_factory=list)

    def add_purchased(self, purchase: str):
        self.purchased.append(purchase)

    def add_treasure(self, treasure: str):
        self.treasure.append(treasure)

    def serialise(self) -> dict:
        return {
            "purchased": self.purchased,
            "treasure": self.treasure,
        }


@dataclass
class Magick:
    name: str
    type: MagickType
    effects: str
    tips: str
    license: str
    job_classes: List[str] = field(default_factory=list)
    find: WhereToFind = field(default_factory=WhereToFind)

    def add_job(self, job: str):
        self.job_classes.append(job)

    def serialise(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "effects": self.effects,
            "tips": self.tips,
            "license": self.license,
            "job_classes": self.job_classes,
            "find": self.find.serialise(),
        }
