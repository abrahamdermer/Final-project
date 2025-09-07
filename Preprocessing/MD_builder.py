from .i_md_builder import I_md_builder
from pathlib import Path



class MD_Builder(I_md_builder):

    @staticmethod
    def get_MD_json(path):
        md ={}
        p = Path(path)
        info = p.stat()
        md['size'] = info.st_size
        md['atime'] = info.st_atime
        # print(info.st_size)
        md['path'] = path
        return md
    
# os.stat_result(st_mode=33206, st_ino=32369622322056294, st_dev=6831590897339041723, st_nlink=1, st_uid=0, st_gid=0, st_size=2331450, st_atime=1757233775, st_mtime=1757230815, st_ctime=315522000)