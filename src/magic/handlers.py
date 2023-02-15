from dataclasses import dataclass, field
from .base import Magick, WhereToFind, MagickType
from typing import List
from json import dumps


@dataclass
class MagicksCollection:
    magicks: List[Magick] = field(default_factory=list)

    def _add_magick(self, magick: Magick):
        self.magicks.append(magick)

    def serialise(self) -> str:
        return dumps([magick.serialise() for magick in self.magicks])


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
            Magick(name, MagickType.ARCANE, effects, tips, license, jobs, find)
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
            Magick(name, MagickType.BLACK, effects, tips, license, jobs, find)
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
            Magick(name, MagickType.GREEN, effects, tips, license, jobs, find)
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
            Magick(name, MagickType.TIME, effects, tips, license, jobs, find)
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
            Magick(name, MagickType.WHITE, effects, tips, license, jobs, find)
        )
