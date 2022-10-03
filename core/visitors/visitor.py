"""

"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.object import SimObject
    from ..objects.root import Root
    from ..objects.Map import Map
    from ..objects.colony import Colony
    from ..objects.agent import Agent


class Visitor(metaclass = ABCMeta):
    def __call__(self, object: SimObject, *args, **kwargs) -> None:
        return object.accept(self, *args, **kwargs)

    @abstractmethod
    def visit_root(self, root: Root) -> Any:
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