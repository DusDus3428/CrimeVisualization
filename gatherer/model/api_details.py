from dataclasses import dataclass


@dataclass
class ApiDetails:
    def __init__(self, url, name, id, key):
        self.url = url
        self.name = name
        self.id = id
        self.key = key