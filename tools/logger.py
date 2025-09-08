import logging
from elasticsearch import Elasticsearch
from datetime import datetime

class Logger:
    _loggre = None

    @classmethod
    def get_logger(cls,name = "",es_host = "",index = '',level = logging.DEBUG):
        if cls._loggre:
            return cls._loggre
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self,record):
                    try:
                        es.index(index=index,document={
                            "timestamp":datetime.utcnow().isoformat(),
                            'level':record.levelname,
                            "logger":record.name,
                            "message":record.getMessage()
                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            
            logger.addHandler(ESHandler)
            logger.addHandler(logging.StreamHandler())
        cls._loggre = logger
        return logger