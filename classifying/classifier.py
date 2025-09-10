from .determining_level import Set_level
from .determining_percent import Set_percent
from .determining_threat import Set_threat
from tools import ESRepository



class Classifier:

    def __init__(self):
        # self.bad_words_1 = []
        # self.bad_words_2 = []
        self.es = ESRepository()

    def to_classifing(self,id)->None:
        Set_percent.to_clessiping()
        Set_threat.to_clessiping()
        Set_level.to_clessiping()