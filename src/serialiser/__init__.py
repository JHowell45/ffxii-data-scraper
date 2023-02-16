from dataclasses import dataclass
from typing import List
from json import dumps


@dataclass
class Serialiser:
    path: str

    def save(self, data: List[dict]):
        with open(self.path, "w") as f:
            f.write(dumps(data, indent=2))

    def load(self) -> List[dict]:
        pass
