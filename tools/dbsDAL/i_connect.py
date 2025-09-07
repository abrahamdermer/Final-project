
from abc import ABC, abstractmethod

class IConnect(ABC):
    """Interface for DB connection objects."""
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self) -> None:
        pass
