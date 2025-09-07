from abc import ABC, abstractmethod
from typing import Callable, Any

MessageHandler = Callable[[str, Any , dict], None]



class IConsumer(ABC):
    """Interface for a Kafka message subscriber."""

#     @abstractmethod
#     def subscribe(self, topics:str|list) -> None:
#         """Subscribe to given topics."""
#         pass

    @abstractmethod
    def listen(self, on_message: MessageHandler) -> None:
        """Start a polling loop and invoke on_message for each record."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the consumer safely (commit if needed)."""
        pass