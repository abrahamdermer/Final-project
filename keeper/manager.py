from tools.kafkaDAL.kafka_consumer import KafkaConsumerRepo


def messageHandler(topic,massage):
    print(f"topic: {topic}, masseg: {massage}")


class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo('to_saving')

    def start_lisane(self):
        self.kafka.listen(messageHandler)

    




    

m = Manager()

m.start_lisane()