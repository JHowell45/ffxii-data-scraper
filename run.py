from src.magic.scraper import (
    ArcaneMagickPage,
    BlackMagickPage,
    GreenMagickPage,
    TimeMagickPage,
    WhiteMagickPage,
)

from alive_progress import alive_bar

from src.serialiser import Serialiser


def save_magick(filepath: str):
    magicks = []
    models = [
        ArcaneMagickPage(),
        BlackMagickPage(),
        GreenMagickPage(),
        TimeMagickPage(),
        WhiteMagickPage(),
    ]
    with alive_bar(len(models)) as bar:
        for scraper in models:
            scraper.load()
            magicks += scraper.get_magicks().serialise()
            bar()
    serial = Serialiser(filepath)
    serial.save(magicks)


if __name__ == "__main__":
    save_magick("./magick.json")
