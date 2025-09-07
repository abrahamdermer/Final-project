from tools.kafkaDAL.kafka_consumer import KafkaConsumerRepo
from tools.dbsDAL.es_repository import ESRepository
es = None


def messageHandler(topic:str,message:dict):
    print(f"topic: {topic}, masseg: {message}")
    path = message.pop('path')
    u_id = '' #  = Create_id.get_uniq_id(message['?'])
    message['u_id'] = u_id
    es.insert(message)
    file = '' # getfile(path)
    # mdb.send(file,u_id)



class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo('to_saving')
        global es
        es = ESRepository()

    def start_lisane(self):
        self.kafka.listen(messageHandler)

    




    

m = Manager()

m.start_lisane()