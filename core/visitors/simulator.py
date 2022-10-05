"""

"""

from __future__ import annotations

from random import choices
from typing import Any, TYPE_CHECKING

from .visitor import Visitor
import settings
from icecream import ic

if TYPE_CHECKING:
    from ..objects.root import Root
    from ..objects.map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent
    from ..objects.food import Food

def eat(agent: Agent, food: Food) -> Agent:
    agent.nutrition += 250
    return agent

class Simulator(Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.i = 0

        # TODO convert to double dispatch for interaction
        if not TYPE_CHECKING:
            from ..objects.agent import Agent
            from ..objects.food import Food
        self.resolutions = {
            (Agent, Agent): lambda a1, a2: a1,
            (Agent, Food): eat,
            (Food, Food): lambda f1, f2: f1,
        }

    def visit_root(self, root: Root) -> Any:  # type: ignore[override]
        self.visit(root.map)
        self.i += 1

    def visit_map(self, map: Map) -> Any:  # type: ignore[override]
        for colony in map.colonies:
            self.visit(colony, map)

        for food in map.food.copy():
            if food not in map.tiles[food.pos]:
                map.food.remove(food)
        
        # input('here')
        for o in map.occupied:
            while len(items := map.tiles[o]) > 1:
                i1 = items.pop()
                i2 = items.pop()
                if res := self.resolutions[type(i1), type(i2)](i1, i2):
                    map.tiles[o].append(res)


    def visit_colony(self, colony: Colony, map: Map) -> Any:  # type: ignore[override]
        for agent in colony.agents:
            self.visit(agent, map, colony)

    def visit_agent(self, agent: Agent, map: Map, colony: Colony) -> Any:  # type: ignore[override]
        if agent.health == 0 and agent.alive:
            agent.kill()
            

        if agent not in map.tiles[agent.pos]:
            # TODO remove from colony
            map.agents.remove(agent)
            colony.agents.remove(agent)
            return  # dead
        dist = 1

        agent.prev_pos = agent.pos

        if agent.mobile:
            agent.pos = (
                max(0, min(settings.MAP_SIZE[0] - 1, agent.pos[0] + choices(range(-dist, dist + 1), weights = (1 if i != 0 else 10 for i in range(-dist, dist + 1)), k = 1)[0])),
                max(0, min(settings.MAP_SIZE[1] - 1, agent.pos[1] + choices(range(-dist, dist + 1), weights = (1 if i != 0 else 10 for i in range(-dist, dist + 1)), k = 1)[0]))
            )

        assert 0 <= agent.pos[0] < settings.MAP_SIZE[0]
        assert 0 <= agent.pos[1] < settings.MAP_SIZE[1]

        if agent.prev_pos != agent.pos:
            map.tiles[agent.prev_pos].remove(agent)
            map.tiles[agent.pos].append(agent)

        
        if agent.nutrition > 1 and agent.health < agent.max_health:
            agent.nutrition -= 2
            agent.health += 1
        else:
            agent.nutrition = max(0, agent.nutrition - 1)
        
        if agent.nutrition == 0:
            agent.health -= 1


        

    def visit_food(self, food: Food) -> Any:  # type: ignore[override]
        pass
