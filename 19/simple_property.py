from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires) -> None:
        self.name = name
        self.expires = expires


    @property
    def expired(self):
        return datetime.now() > self.expires
