"""

"""

from typing import Any

from ..visitors import Visitor
from .object import SimObject


class Agent(SimObject):
   def __init__(self, pos: tuple[int, int]) -> None:
      super().__init__()
      self.pos = pos

   def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
      return visitor.visit_agent(self, *args, **kwargs)
