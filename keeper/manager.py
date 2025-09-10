from tools import KafkaConsumerRepo ,ESRepository ,MongoRepository ,UniqID ,KafkaProducerRepo
import threading
import time
from . import config

producer:KafkaProducerRepo|None = None
es:ESRepository|None = None
mongodb:MongoRepository|None = None


def messageHandler(topic:str,message:dict):
    # print(f"topic: {topic}, masseg: {message}")
    path:str = message.pop('path')
    u_id = UniqID.get_id(message['atime'],message['size'])
    message['u_id'] = u_id
    es.insert(message)
    data = {}
    with open(path, 'rb') as f:
        data['file'] = f
        data['name'] = path.split('\\')[-1]
        data['metadata'] = {'u_id':u_id}
        mongodb.insert_gridfs(data)
    producer.send(config.TARGET_TOPIC_NAME,{'u_id':u_id})
    

class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo(config.SOURCE_TOPIC_NAME)
        global es , mongodb,producer
        producer = KafkaProducerRepo()
        es = ESRepository()
        mongodb = MongoRepository()

    def start_lisane(self,messageHandler):
        t = threading.Thread(target=self.kafka.listen,args=(1,messageHandler),daemon=True)
        t.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("stop thred")


    
if __name__ == "__main__":
    m = Manager()

    m.start_lisane(messageHandler)