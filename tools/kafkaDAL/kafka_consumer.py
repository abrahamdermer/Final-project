import json
from typing import  Any
from kafka.errors import KafkaError as KafkaLibError
from .i_consumer import IConsumer, MessageHandler
from .kafka_connect import KafkaConnect


def _decode(raw:Any) -> Any:
    if raw is None or not isinstance(raw,bytes):
        return raw
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return raw.decode("utf-8", errors="replace")

class KafkaConsumerRepo(IConsumer):
    """High-level consumer wrapper using kafka.KafkaConsumer."""

    def __init__(self,topics: str|list[str], conn:KafkaConnect|None = None) -> None:
        self._conn = conn or KafkaConnect()
        self._consumer = self._conn.get_consumer(topics)

    # def subscribe(self, topics: str|list[str]) -> None:
    #     if isinstance(topics ,str):
    #         topics = [topics]
    #     self._consumer.subscribe(topics)


    def listen(self,n, on_message: MessageHandler) -> None:
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        try:
            for msg in self._consumer:
                print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
                value = _decode(msg.value)
                on_message(msg.topic, value)
        except enumerate as exc:
            raise (f"Consumer listen failed: {exc}")
        finally:
            self.close()


    def close(self) -> None:
        try:
            self._consumer.close()
        except Exception:
            pass