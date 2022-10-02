"""

"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .visitor import Visitor

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.Map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent


class Renderer(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.canvas = None

    def visit_root(self, root: Root) -> Any:  # type: ignore[override]
        return self(root.map)

    def visit_map(self, map: Map) -> Any:  # type: ignore[override]
        for agent in map.agents:
            self(agent)

    def visit_colony(self, colony: Colony) -> Any:  # type: ignore[override]
        pass

    def visit_agent(self, agent: Agent) -> Any:  # type: ignore[override]
        pass