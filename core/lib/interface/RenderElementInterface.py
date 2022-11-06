from __future__ import annotations
from abc import ABC, abstractmethod


class RenderElementInterface(ABC):

    @abstractmethod
    def render(self, data, type) -> None:
        pass
