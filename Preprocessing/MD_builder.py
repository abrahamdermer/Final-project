from .i_md_builder import I_md_builder



class MD_Builder(I_md_builder):

    @staticmethod
    def get_MD_json(path):
        md ={}
        md['path'] = path
        # print(path)
        return md