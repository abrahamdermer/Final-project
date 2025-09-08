from tools.kafkaDAL.kafka_consumer import KafkaConsumerRepo
from tools.dbsDAL.es_repository import ESRepository
from tools.dbsDAL.mongo_repository import MongoRepository
from tools.create_u_id import UniqID
import threading
import time


es = None
mongodb:MongoRepository|None = None

def messageHandler(topic:str,message:dict):
    print(f"topic: {topic}, masseg: {message}")
    path:str = message.pop('path')
    u_id = UniqID.get_id(message['atime'],message['size'])
    message['u_id'] = u_id
    es.insert(message)
    data = {}
    with open(path, 'rb') as f:
        data['file'] = f
        data['name'] = path.split('\\')[-1]
        data['metadata'] = {'u_id':u_id}
        print(data)
        mongodb.insert_gridfs(data)

# return self.fs.upload_from_stream(data['name'], data['file'], metadata=data['metadata'])
# with open('your_file.txt', 'rb') as f:
#         file_id = fs.upload_from_stream('your_file.txt', f)
#         # You can also add metadata:
#         # file_id = fs.upload_from_stream('your_file.txt', f, metadata={'author': 'John Doe'})    


class Manager:

    def __init__(self):
        self.kafka = KafkaConsumerRepo('to_saving')
        global es , mongodb
        es = ESRepository()
        mongodb = MongoRepository()

    def start_lisane(self,messageHandler):
        # self.kafka.listen(messageHandler)
        t = threading.Thread(target=self.kafka.listen,args=(1,messageHandler),daemon=True)
        t.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("stop thred")

    # def run(self):
    #     t = threading.Thread(target=self.start_lisane,args=(messageHandler),daemon=True)
    #     t.start()
    #     try:
    #         while True:
    #             time.sleep(1)
    #     except KeyboardInterrupt:
    #         print("stop thred")
    




    
if __name__ == "__main__":
    m = Manager()

    m.start_lisane(messageHandler)

    # mongodb.get_all()