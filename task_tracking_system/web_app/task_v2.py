from __future__ import annotations

from abc import ABC, abstractmethod

from models.models import User, Task, Session, Base
from sqlalchemy.orm.exc import NoResultFound


class TaskHandler:
    def __init__(self, strategy: InteractionStrategy) -> None:
        self._strategy = strategy
        self.active_user = None
        self.active_task = None
        self.session = Session()
        Base.metadata.create_all()

    @property
    def strategy(self) -> InteractionStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: InteractionStrategy) -> None:
        self._strategy = strategy

    def create_user(self, name) -> None:
        self._strategy.create_user(name)


class InteractionStrategy(ABC):
    @abstractmethod
    def create_user(self, name: str):
        pass


class CommandLineInterface(InteractionStrategy):
    def create_user(self, name: str):
        self.active_user = User(name=name)
        self.session.add(self.active_user)
        self.session.commit()
        print(f'User created: {self.active_user}')
        return self.active_user
