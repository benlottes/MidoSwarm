"""

"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.object import SimObject
    from ..objects.root import Root
    from ..objects.map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent
    from ..objects.food import Food


class Visitor(metaclass = ABCMeta):
    def visit(self, object: SimObject, *args, **kwargs) -> None:
        return object.accept(self, *args, **kwargs)

    @abstractmethod
    def visit_root(self, root: Root, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def visit_map(self, map: Map, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def visit_colony(self, colony: Colony, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def visit_agent(self, agent: Agent, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def visit_food(self, food: Food, *args, **kwargs) -> Any:
        raise NotImplementedError
