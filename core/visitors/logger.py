"""

"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from .visitor import Visitor

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.Map import Map
    from ..objects.agent import Agent


class Logger(Visitor):
    def visit_root(self, root: Root) -> Any:  # type: ignore[override]
        pass  # TODO

    def visit_map(self, map: Map) -> Any:  # type: ignore[override]
        pass  # TODO

    def visit_colony(self, agent: Agent) -> Any:  # type: ignore[override]
        pass  # TODO

    def visit_agent(self, agent: Agent) -> Any:  # type: ignore[override]
        pass  # TODO
