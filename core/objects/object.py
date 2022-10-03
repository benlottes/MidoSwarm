"""

"""

from abc import ABCMeta, abstractmethod
from typing import Any

from ..visitors import Visitor


class SimObject(metaclass = ABCMeta):
    
    @abstractmethod
    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        raise NotImplementedError