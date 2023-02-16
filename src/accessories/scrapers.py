from .handlers import Accessories


class AccessoriesPage:
    def __init__(self) -> None:
        self.url = "https://jegged.com/Games/Final-Fantasy-XII/Equipment-and-Items/Accessories/"
        self.accessories = Accessories()
