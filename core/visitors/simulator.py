"""

"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from .visitor import Visitor

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.Map import Map
    from ..objects.agent import Agent


class Simulator(Visitor):
    def visit_root(self, root: Root) -> Any:  # type: ignore[override]
        self(root.map)

    def visit_map(self, map: Map) -> Any:  # type: ignore[override]
        for agent in map.agents:
            self(agent, map)
        map.print()

    def visit_colony(self, colony: Agent, ctx: Any) -> Any:  # type: ignore[override]
        print(colony)

    def visit_agent(self, agent: Agent, ctx: Any) -> Any:  # type: ignore[override]
        print(agent)