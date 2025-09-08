




class UniqID:

    @staticmethod
    def get_id(atime,size):
        return int(f"{int(atime)}{size}")