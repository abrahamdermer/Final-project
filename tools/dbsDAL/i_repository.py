from abc import ABC, abstractmethod
from typing import Any

class IRepository(ABC):
    """Repository interface with CRUD-like methods."""

    @abstractmethod
    def insert(self, data: dict[str, Any]) -> Any:
        pass

    # @abstractmethod
    # def find(self, query: dict[str, Any]) -> Any:
    #     pass

    # @abstractmethod
    # def update(self, query: dict[str, Any], new_values: dict[str, Any]) -> Any:
    #     pass

    # @abstractmethod
    # def delete(self, query: dict[str, Any]) -> Any:
    #     pass
