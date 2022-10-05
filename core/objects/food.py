"""

"""

from typing import Any

from ..visitors import Visitor
from .object import SimObject


class Food(SimObject):
   def __init__(self, pos: tuple[int, int]) -> None:
      super().__init__()
      self.pos = pos
      self.nutrition_value = 250

   def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
      return visitor.visit_food(self, *args, **kwargs)

   def interact(self, actor):
      return actor.interact_food(self)

   def interact_agent(self, agent):
      return agent.interact_food(self)

   def interact_food(self, food):
      self.nutrition_value += food.nutrition_value
      return self