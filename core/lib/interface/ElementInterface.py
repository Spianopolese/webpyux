from MediatorInterface import MediatorInterface


class ElementInterface:

    def __init__(self, mediator: MediatorInterface = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> MediatorInterface:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: MediatorInterface) -> None:
        self._mediator = mediator
