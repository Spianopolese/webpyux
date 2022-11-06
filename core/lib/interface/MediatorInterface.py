from __future__ import annotations
from abc import ABC


class MediatorInterface(ABC):

    def notify(self, sender: object, event: str) -> None:
        pass
