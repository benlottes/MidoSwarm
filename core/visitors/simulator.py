"""

"""

from __future__ import annotations

from random import choices
from typing import Any, TYPE_CHECKING

from .visitor import Visitor
import settings

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.Map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent


class Simulator(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.i = 0

    def visit_root(self, root: Root) -> Any:  # type: ignore[override]
        self.visit(root.map)
        self.i += 1

    def visit_map(self, map: Map) -> Any:  # type: ignore[override]
        for colony in map.colonies:
            self.visit(colony)

    def visit_colony(self, colony: Colony) -> Any:  # type: ignore[override]
        for agent in colony.agents:
            self.visit(agent)

    def visit_agent(self, agent: Agent) -> Any:  # type: ignore[override]
        dist = 1
        
        agent.pos = (
            max(0, min(settings.MAP_SIZE[0] - 1, agent.pos[0] + choices(range(-dist, dist + 1), weights = (1 if i != 0 else 25 for i in range(-dist, dist + 1)), k = 1)[0])),
            max(0, min(settings.MAP_SIZE[1] - 1, agent.pos[1] + choices(range(-dist, dist + 1), weights = (1 if i != 0 else 25 for i in range(-dist, dist + 1)), k = 1)[0]))
        )
        assert 0 <= agent.pos[0] < settings.MAP_SIZE[0]
        assert 0 <= agent.pos[1] < settings.MAP_SIZE[1]
