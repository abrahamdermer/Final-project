from abc import ABC, abstractmethod
from typing import Any

class IConnect(ABC):
    """
    Interface for establishing Kafka connections.
    Provides factory methods to create producer/consumer instances.
    """
    @abstractmethod
    def get_producer(self) -> Any:
        """Return a KafkaProducer instance."""
        pass

    @abstractmethod
    def get_consumer(self,topics:list[str]|str = None) -> Any:
        """Return a KafkaConsumer instance; if topics provided, subscribe immediately."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close any shared resources if applicable."""
        pass
