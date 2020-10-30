from datetime import datetime


class Item:
    def __init__(self, location: str, name: str):
        self.location = location
        self.name = name
        self.creationDate = datetime.now()
