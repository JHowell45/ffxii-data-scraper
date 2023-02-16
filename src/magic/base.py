from dataclasses import dataclass, field
from typing import List
from enum import Enum
from src.shared import WhereToFind


class MagickType(Enum):
    ARCANE = "arcane"
    BLACK = "black"
    GREEN = "green"
    TIME = "time"
    WHITE = "white"


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
