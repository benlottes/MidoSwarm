"""

"""

from typing import Any

from ..visitors import Visitor
from .object import SimObject
from .agent import Agent


class Colony(SimObject):
    def __init__(self, num_agents: int) -> None:
        self.starting_agents = num_agents
        self.num_agents = self.starting_agents
        self.agents = [Agent() for _ in range(num_agents)]

    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        return visitor.visit_colony(self, *args, **kwargs)
