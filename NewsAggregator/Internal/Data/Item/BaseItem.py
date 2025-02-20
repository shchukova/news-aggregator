
from NewsAggregator.Internal.Data.IItem import IItem

class BaseItem(IItem):
    __id = None
    __name = None
    __type = None

    def __init__(self, id: int, name: str, type: str):
        self.__id = id
        self.__name = name
        self.__type = type

    def get_id() -> int:
        return self.__id

    def get_name() -> str:
        return self.__name

    def get_type() -> int:
        return self.__type