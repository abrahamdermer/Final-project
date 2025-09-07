from abc import ABC, abstractmethod
from typing import Any, Mapping, Optional

class IProducer(ABC):
    """Interface for a Kafka message publisher."""

    @abstractmethod
    def send(self,topic: str,value: Any,) -> None:
        """Publish a message to a topic."""
        pass

    @abstractmethod
    def flush(self) -> None:
        """Ensure all buffered messages are delivered."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the underlying producer safely."""
        pass