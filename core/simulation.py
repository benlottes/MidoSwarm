"""

"""

from core.objects.root import Root
from core.visitors import Visitor

class Simulation:
    def __init__(self, visitors: list[Visitor]) -> None:
        self.visitors = visitors
        self.root = Root()

    def step(self) -> None:
        for visitor in self.visitors:
            visitor(self.root)
