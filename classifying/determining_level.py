from .i_determining import IDetermining



class Set_level(IDetermining):
    script = {
        "source": "ctx._source.bds_threat_level = params.new_value",
        "lang": "painless",
        "params": {
            "new_value": 'none'
        }
    }

    
    @staticmethod
    def to_clessiping(es,id)->None:
        query ={
            "term": {
                "u_id": id
            }
        }
        body = {"query": query, "script": Set_level.script}
        es.update_by_script(body)