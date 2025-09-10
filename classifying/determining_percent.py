from .i_determining import IDetermining



class Set_percent(IDetermining):
    
    script = {
        "source": "ctx._source.bds_percent = params.new_value",
        "lang": "painless",
        "params": {
            "new_value": 0.00000000001
        }
    }

    
    @staticmethod
    def to_clessiping(es,id,very_bad_words,less_bad_words)->None:
        query ={
            "term": {
                "u_id": id
            }
        }
        body = {"query": query, "script": Set_percent.script}
        es.update_by_script(body)