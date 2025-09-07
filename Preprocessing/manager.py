from os import listdir
from os.path import isfile, join
from .MD_builder import MD_Builder
from tools.kafkaDAL.kafka_producer import KafkaProducerRepo

# mypath ="C:\podcasts"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)



class Manager:

    def __init__(self,mypath = "C:\podcasts"):
        self.topic_name = "to_saving"
        self.mypath =mypath
        self.files = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        self.kafka = KafkaProducerRepo()

    def create_md(self):
        md = {}
        for f in self.files:
            md[f] = MD_Builder.get_MD_json(f"{self.mypath}\{f}")
        self.files_pals_md = md
        # print(self.files_pals_md)

    def send(self):
        for v in self.files_pals_md.values():
            print(v)
            self.kafka.send(self.topic_name,v)



m = Manager()
m.create_md()
m.send()

m.create_md()