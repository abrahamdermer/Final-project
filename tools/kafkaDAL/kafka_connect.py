from kafka import KafkaProducer, KafkaConsumer
from .i_connect import IConnect

class KafkaConnect(IConnect):
    """
    Concrete Kafka connection factory.
    Creates KafkaProducer and KafkaConsumer with sane defaults from config.
    """

    def __init__(self, bootstrap_servers:str = "localhost:9092",group_id = 'mygroup') -> None:
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
       

    def get_producer(self) -> KafkaProducer:
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            client_id= "kafka-dal-client"
        )
        return producer

    def get_consumer(self,topics:list[str]|str) -> KafkaConsumer:
        if isinstance(topics ,str):
            topics = [topics]
        consumer = KafkaConsumer(
            bootstrap_servers=self.bootstrap_servers,
            # client_id =
            group_id = self.group_id,
            auto_offset_reset="latest"
        )
        consumer.subscribe(topics)
        return consumer

    def close(self) -> None:
        return None
