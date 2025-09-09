from tools import KafkaConsumerRepo ,ESRepository ,MongoRepository  , Logger
import threading
import time
from .transcriber import Transcriber


es:ESRepository|None = None
mongodb:MongoRepository|None = None
transc:Transcriber = None

def messageHandler(topic:str,message:dict):
    # print(f"topic: {topic}, masseg: {message}")
    u_id = message["u_id"]
    query = {'u_id':u_id}
    file = mongodb.find_gridfs(query)
    text = transc.file_to_text(file,u_id)
    print(text)
    query = {"match":{'u_id':u_id}}
    print(es.update(query,{'text':text}))
    

class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo('to_transcribing')
        global es , mongodb,transc
        transc = Transcriber()
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

    # mongodb.get_all()