"""

"""

from typing import Any

from ..visitors import Visitor
from .object import SimObject


class Agent(SimObject):
   
   def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
      return visitor.visit_agent(self, *args, **kwargs)
