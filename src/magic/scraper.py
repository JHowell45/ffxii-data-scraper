from bs4 import BeautifulSoup
from requests import get


class ArcaneMagickPage:
    def __init__(self) -> None:
        self.url = (
            "https://jegged.com/Games/Final-Fantasy-XII/Magick/Arcane-Magick.html"
        )

    def load_magicks_table(self):
        page = get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="nav-tabContent")
        results = soup.find(id="nav-standard")
        for spell in results.find_all("div", class_="card"):
            # print(spell)
            name = spell.find(
                "div", class_="card-header walkthrough-object-header"
            ).find("a")["name"]
            effects, tips, jobs, license, find = [note for note in spell.find_all("dd")]
            print(name)
            print(effects)
            print(tips)
            print(find)
            print(license)
            print(find)
            # print(name)
            print(200 * "#")
