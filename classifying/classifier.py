from .determining_level import Set_level
from .determining_percent import Set_percent
from .determining_threat import Set_threat
from tools import ESRepository
import base64



class Classifier:

    def __init__(self):
        # self.bad_words_1 = []
        # self.bad_words_2 = []
        self.es = ESRepository()
        self.very_bad_words = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'
        self.less_bad_words = 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ'
    
    def myencode(self,text:str):

        data = base64.b64decode(text).decode("ascii")
        words = data.split(',')
        return words




    def to_classifing(self,id)->None:
        Set_percent.to_clessiping(self.es,id,self.myencode(self.very_bad_words),self.myencode(self.leas_bad_words))
        Set_threat.to_clessiping(self.es,id)
        Set_level.to_clessiping(self.es,id)