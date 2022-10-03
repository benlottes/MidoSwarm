"""

"""

from typing import Any

from ..visitors import Visitor
from .Map import Map
from .object import SimObject
import settings


class Root(SimObject):
    def __init__(self) -> None:
        super().__init__()
        self.map = Map(settings.MAP_SIZE, 10, 10, 10, 10)

    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        return visitor.visit_root(self, *args, **kwargs)
