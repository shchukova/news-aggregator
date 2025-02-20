from abc import ABCMeta, abstractmethod
from NewsAggregator.Internal.Data.IItem import IItem

class ICollection(metaclass=ABCMeta):
    
    TYPE_NEWS = 1

    @abstractmethod
    def append_item(item: IItem):
        pass