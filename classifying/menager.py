from tools import KafkaConsumerRepo ,ESRepository ,MongoRepository  , Logger
import threading
import time
from .classifier import Classifier
from . import config


es:ESRepository|None = None
mongodb:MongoRepository|None = None
classifier:Classifier|None = None

def messageHandler(fike:int,message:dict):
    # print(f"topic: {topic}, masseg: {message}")
    u_id = message["u_id"]
    # classifier.to_classing(u_id)
    

class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo(config.SOURCE_TOPIC_NAME)
        global es , mongodb ,classifier
        classifier = Classifier()
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