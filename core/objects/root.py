"""

"""

from typing import Any

from ..visitors import Visitor
from .Map import Map
from .object import SimObject


class Root(SimObject):
    def __init__(self) -> None:
        super().__init__()
        self.map = Map(10, 10, 10, 10, 10)

    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        return visitor.visit_root(self, *args, **kwargs)
