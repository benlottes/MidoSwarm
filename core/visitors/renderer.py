"""

"""

from __future__ import annotations

import os.path as osp, os
from typing import Any, TYPE_CHECKING

from .visitor import Visitor
from ..graphics.engine import TileEngine
import settings

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent
    from ..objects.food import Food


class Renderer(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.engine = TileEngine(
            (int(0.6 * 1920), int(0.6 * 1080)),
            settings.MAP_SIZE,
            'MidoSwarm',
            target_fps = 24,
            record_path = osp.join('core', 'graphics')
        )
        self.colony_color_options = (
            (75, 253, 253),
            (190, 27, 2),
            (208, 201, 30),
            (61, 0, 194),
            (4, 133, 208),
            (254, 56, 129),
            (3, 254, 126),
            (3, 180, 0),
            (179, 60, 254),
        )

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
        for food in map.food:
            self.visit(food)
        
        for i, colony in enumerate(map.colonies):
            self.visit(colony, i)

    def visit_colony(self, colony: Colony, colony_idx: int) -> Any:  # type: ignore[override]
        for agent in colony.agents:
            self.visit(agent, self.colony_color_options[colony_idx])

    def visit_agent(self, agent: Agent, color: tuple[int, int, int]) -> Any:  # type: ignore[override]
        if agent.alive:
            self.engine.render_circle(self.engine.scale_up(agent.pos), self.engine.grid_size[0] / 2, color)
        else:
            self.engine.render_circle(self.engine.scale_up(agent.pos), self.engine.grid_size[0] / 2, (100, 100, 100))
        # self.engine.render_rect(self.engine.scale_up(agent.pos), self.engine.grid_size, color)

    def visit_food(self, food: Food) -> Any:  # type: ignore[override]
        self.engine.render_rect(self.engine.scale_up(food.pos), self.engine.grid_size, self.engine.colors['green'])