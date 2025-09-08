from .i_md_builder import I_md_builder
from pathlib import Path



class MD_Builder(I_md_builder):

    @staticmethod
    def get_MD_json(path:str):
        md ={}
        p = Path(path)
        info = p.stat()
        md['size'] = info.st_size
        md['atime'] = info.st_atime
        md['path'] = path
        return md