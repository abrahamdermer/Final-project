from .i_determining import IDetermining



class Set_threat(IDetermining):

    script = {
        "source": "ctx._source.is_bds = params.new_value",
        "lang": "painless",
        "params": {
            "new_value": False
        }
    }

    
    @staticmethod
    def to_clessiping(es,id)->None:
        query ={
            "term": {
                "u_id": id
            }
        }
        body = {"query": query, "script": Set_threat.script}
        es.update_by_script(body)