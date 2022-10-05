"""

"""

from typing import Any

from ..visitors import Visitor
from .object import SimObject


class Agent(SimObject):
   def __init__(self, pos: tuple[int, int], nutrition: int, health: int, max_health: int) -> None:
      super().__init__()
      self.prev_pos = None
      self.pos = pos
      self.nutrition = nutrition
      self.health = health
      self.max_health = max_health
      self.alive = True
      self.mobile = True

   def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
      return visitor.visit_agent(self, *args, **kwargs)

   def interact(self, actor, *args, **kwargs):
      return actor.interact_agent(self, *args, **kwargs)

   def interact_agent(self, agent):
      return self

   def interact_food(self, food):
      self.nutrition += food.nutrition_value
      return self

   def kill(self) -> None:
      self.alive = False
      self.mobile = False