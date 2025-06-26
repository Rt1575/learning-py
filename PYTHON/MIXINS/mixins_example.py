class WalkMixin:
    def walk(self):
        return f"{self.name} is walking."

class TalkMixin:
    def talk(self):
        return f"{self.name} says hello."

class Person(WalkMixin, TalkMixin):
    def __init__(self, name):
        self.name = name
