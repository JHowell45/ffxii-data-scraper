from bs4 import BeautifulSoup
from requests import get
from typing import Generator
from .handlers import (
    ArcaneMagicks,
    BlackMagicks,
    WhiteMagicks,
    TimeMagicks,
    GreenMagicks,
    MagicksCollection,
)
from src.shared import WhereToFind


class MagickPage:
    def __init__(self, url: str, magicks: MagicksCollection) -> None:
        self.url = url
        self.magicks = magicks

    def load_magicks_table(self) -> Generator[dict, None, None]:
        page = get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="nav-tabContent")
        results = soup.find(id="nav-standard")
        for spell in results.find_all("div", class_="card"):
            name = spell.find(
                "div", class_="card-header walkthrough-object-header"
            ).find("a")["name"]
            effects, tips, jobs, license, find = [note for note in spell.find_all("dd")]
            current_key = ""
            find_data = {}
            for item in find.find_all():
                if item.name == "strong":
                    match item.string.lower():
                        case "purchased from:":
                            current_key = "purchased"
                        case "bazaar:":
                            current_key = "bazaar"
                        case "stolen from:":
                            current_key = "stolen"
                        case "treasure:":
                            current_key = "treasure"
                        case "side quest:":
                            current_key = "side_quest"
                        case "poached from:":
                            current_key = "poached"
                        case _:
                            current_key = item.string
                if item.name == "a":
                    if current_key in find:
                        find_data[current_key] = find_data[current_key].append(
                            item.string
                        )
                    else:
                        find_data[current_key] = [item.string]
            yield {
                "name": name,
                "effects": effects.string,
                "tips": tips.string,
                "jobs": jobs.string,
                "license": license.string,
                "find": find_data,
            }

    def load(self):
        for data in self.load_magicks_table():
            self.magicks.add_magick(
                name=data["name"],
                effects=data["effects"],
                tips=data["tips"],
                jobs=data["jobs"],
                license=data["license"],
                find=WhereToFind.from_dict(data["find"]),
            )

    def get_magicks(self) -> MagicksCollection:
        return self.magicks


class ArcaneMagickPage(MagickPage):
    def __init__(self) -> None:
        super().__init__(
            "https://jegged.com/Games/Final-Fantasy-XII/Magick/Arcane-Magick.html",
            ArcaneMagicks(),
        )


class BlackMagickPage(MagickPage):
    def __init__(self) -> None:
        super().__init__(
            "https://jegged.com/Games/Final-Fantasy-XII/Magick/Black-Magick.html",
            BlackMagicks(),
        )


class GreenMagickPage(MagickPage):
    def __init__(self) -> None:
        super().__init__(
            "https://jegged.com/Games/Final-Fantasy-XII/Magick/Green-Magick.html",
            GreenMagicks(),
        )


class TimeMagickPage(MagickPage):
    def __init__(self) -> None:
        super().__init__(
            "https://jegged.com/Games/Final-Fantasy-XII/Magick/Time-Magick.html",
            TimeMagicks(),
        )


class WhiteMagickPage(MagickPage):
    def __init__(self) -> None:
        super().__init__(
            "https://jegged.com/Games/Final-Fantasy-XII/Magick/White-Magick.html",
            WhiteMagicks(),
        )
