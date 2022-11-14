"""

"""

from typing import Any
from enum import Enum
from ..visitors import Visitor
from .object import SimObject

Directions = Enum('Direction', "N NW W SW S SE E NE")

class Agent(SimObject):

   def __init__(self, pos: tuple[int, int], nutrition: int, health: int, max_health: int) -> None:
      super().__init__()
      self.dir = Directions.NW
      self.prev_pos = None
      self.pos = pos
      self.vision_map = [[0 for _ in range(41)] for _ in range(41)]
      self.nutrition = nutrition
      self.health = health
      self.max_health = max_health
      self.alive = True
      self.mobile = True

   def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
      return visitor.visit_agent(self, *args, **kwargs)

   def kill(self) -> None:
      self.alive = False
      self.mobile = False

   def change_dir(self, update_dir: int) -> None:
      self.dir = Directions(self.dir.value + update_dir)

   def look(self, map: dict) -> list:
      pass