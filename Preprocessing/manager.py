from os import listdir
from os.path import isfile, join
from .MD_builder import MD_Builder
from tools import KafkaProducerRepo
from . import config
# from tools import  Logger


class Manager:

    def __init__(self,mypath:str = config.FILE_PATH):
        # self.logger = Logger.get_logger()
        self.topic_name = config.TARGET_TOPIC_NAME
        self.mypath =mypath
        self.files = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
        self.kafka = KafkaProducerRepo()

    def create_md(self):
        md = {}
        for f in self.files:
            md[f] = MD_Builder.get_MD_json(f"{self.mypath}\{f}")
        self.files_pals_md = md
        # self.logger.info("Metadata has been created for all files.")

    def send(self):
        for k, v in self.files_pals_md.items():
            self.kafka.send(self.topic_name,v)
            print(f"Metadata for {k} sent to Kafka")
            # self.logger.info(f"Metadata for {k} sent to Kafka")



m = Manager()
m.create_md()
m.send()



