"""

"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

from .visitor import Visitor
from ..graphics.engine import TileEngine
import settings

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.Map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent


class Renderer(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.engine = TileEngine((int(0.6 * 1920), int(0.6 * 1080)), settings.MAP_SIZE, 'MidoSwarm', target_fps=24)

    def visit_root(self, root: Root) -> Any:  # type: ignore[override]
        if self.engine.should_run():
            self.engine.clear_screen()
            self.engine.render_rect(
                self.engine.scale_up((0, 0)),
                (self.engine.grid_size[0] * self.engine.num_grids[0], self.engine.grid_size[1] * self.engine.num_grids[1]),
                self.engine.colors['white']
            )
            self.visit(root.map)
            self.engine.update_screen()

    def visit_map(self, map: Map) -> Any:  # type: ignore[override]
        for colony in map.colonies:
            self.visit(colony)

    def visit_colony(self, colony: Colony) -> Any:  # type: ignore[override]
        for agent in colony.agents:
            self.visit(agent)

    def visit_agent(self, agent: Agent) -> Any:  # type: ignore[override]
        self.engine.render_circle(self.engine.scale_up(agent.pos), self.engine.grid_size[0] / 2, TileEngine.colors['red'])
        # self.engine.render_rect(self.engine.scale_up(agent.pos), self.engine.grid_size, TileEngine.colors['red'])
