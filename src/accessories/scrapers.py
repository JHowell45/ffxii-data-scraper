from .handlers import Accessories
from src.shared import WhereToFind
from requests import get
from bs4 import BeautifulSoup


class AccessoriesPage:
    def __init__(self) -> None:
        self.url = "https://jegged.com/Games/Final-Fantasy-XII/Equipment-and-Items/Accessories/"
        self.accessories = Accessories()

    def load_accessories_tables(self):
        page = get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="nav-tabContent")
        results = soup.find(id="nav-standard")
        for spell in results.find_all("div", class_="card"):
            name = spell.find(
                "div", class_="card-header walkthrough-object-header"
            ).find("a")["name"]
            effects, other_stats, license, find = [
                note for note in spell.find_all("dd")
            ]
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
            print(other_stats)
            if other_stats.string == "-" or other_stats.string is None:
                other_stats = []
            else:
                other_stats = [stat.strip() for stat in other_stats.string.split(",")]
            yield {
                "name": name,
                "effects": effects.string,
                "other_stats": other_stats,
                "license": license.string,
                "find": find_data,
            }

    def load(self):
        for data in self.load_accessories_tables():
            print(data)
            self.accessories.add_accessory(
                name=data["name"],
                effects=data["effects"],
                other_stats=data["other_stats"],
                license=data["license"],
                find=WhereToFind.from_dict(data["find"]),
            )
