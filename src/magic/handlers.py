from dataclasses import dataclass, field
from .base import Magick, MagickType
from typing import List
from json import dumps
from src.shared import WhereToFind


@dataclass
class MagicksCollection:
    magicks: List[Magick] = field(default_factory=list)

    def _add_magick(self, magick: Magick):
        self.magicks.append(magick)

    def get_magicks(self) -> List[Magick]:
        return self.magicks

    def serialise(self) -> dict:
        return [magick.serialise() for magick in self.magicks]


@dataclass
class ArcaneMagicks(MagicksCollection):
    def add_magick(
        self,
        name: str,
        effects: str,
        tips: str,
        jobs: List[str],
        license: str,
        find: WhereToFind,
    ):
        self._add_magick(
            Magick(name, MagickType.ARCANE.value, effects, tips, license, jobs, find)
        )


@dataclass
class BlackMagicks(MagicksCollection):
    def add_magick(
        self,
        name: str,
        effects: str,
        tips: str,
        jobs: List[str],
        license: str,
        find: WhereToFind,
    ):
        self._add_magick(
            Magick(name, MagickType.BLACK.value, effects, tips, license, jobs, find)
        )


@dataclass
class GreenMagicks(MagicksCollection):
    def add_magick(
        self,
        name: str,
        effects: str,
        tips: str,
        jobs: List[str],
        license: str,
        find: WhereToFind,
    ):
        self._add_magick(
            Magick(name, MagickType.GREEN.value, effects, tips, license, jobs, find)
        )


@dataclass
class TimeMagicks(MagicksCollection):
    def add_magick(
        self,
        name: str,
        effects: str,
        tips: str,
        jobs: List[str],
        license: str,
        find: WhereToFind,
    ):
        self._add_magick(
            Magick(name, MagickType.TIME.value, effects, tips, license, jobs, find)
        )


@dataclass
class WhiteMagicks(MagicksCollection):
    def add_magick(
        self,
        name: str,
        effects: str,
        tips: str,
        jobs: List[str],
        license: str,
        find: WhereToFind,
    ):
        self._add_magick(
            Magick(name, MagickType.WHITE.value, effects, tips, license, jobs, find)
        )
