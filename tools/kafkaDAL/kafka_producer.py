import json
from typing import Any
from .i_producer import IProducer
from .kafka_connect import KafkaConnect
# from tools import Logger

def _encode_value(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False).encode("utf-8")



class KafkaProducerRepo(IProducer):
    """High-level producer wrapper using kafka.KafkaProducer."""

    def __init__(self, conn:KafkaConnect|None = None) -> None:
        self._conn = conn or KafkaConnect()
        self._producer = self._conn.get_producer()
        # self.logger = Logger.get_logger()

    def send(self,topic: str,value: Any,) -> None:
        future = self._producer.send(topic=topic,value=_encode_value(value),)
        future.get(timeout=30)
        # self.logger.info(f"A message has been sent to the topic: {topic}")
        
    def flush(self) -> None:
        self._producer.flush()

    def close(self) -> None:
        try:
            self._producer.flush()
        finally:
            self._producer.close()
