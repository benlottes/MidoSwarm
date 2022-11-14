"""

"""

from typing import Any

from ..visitors import Visitor
from .map import Map
from .object import SimObject
import settings


class Root(SimObject):
    def __init__(self) -> None:
        super().__init__()
        self.map = Map(settings.MAP_SIZE, settings.NUM_FOOD, 10, settings.NUM_COLONIES, settings.AGENTS_PER_COLONY)

    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        return visitor.visit_root(self, *args, **kwargs)
