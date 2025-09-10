from abc import ABC , abstractmethod


class I_md_builder(ABC):

    @staticmethod
    @abstractmethod
    def get_MD_json(path):
        pass