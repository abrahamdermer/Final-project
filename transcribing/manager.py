from tools import KafkaConsumerRepo ,ESRepository ,MongoRepository  , KafkaProducerRepo
import threading
import time
from .transcriber import Transcriber
from . import config


es:ESRepository|None = None
mongodb:MongoRepository|None = None
transc:Transcriber|None = None
producer:KafkaProducerRepo|None = None

def messageHandler(fice:int,message:dict):
    u_id = message["u_id"]
    query = {'u_id':u_id}
    file = mongodb.find_gridfs(query)
    text = transc.file_to_text(file,u_id)
    print(text)
    query = {"match":{'u_id':u_id}}
    print(es.update(query,{'text':text}))
    producer.send(config.TARGET_TOPIC_NAME,{'u_id':u_id})

    

class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo(config.SOURCE_TOPIC_NAME)
        global es , mongodb,transc,producer
        transc = Transcriber()
        es = ESRepository()
        mongodb = MongoRepository()
        producer = KafkaProducerRepo()

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