from abc import ABCMeta, abstractmethod
from NewsAggregator.Internal.Data.Collection.NewsCollection import NewsCollection

class IStorage(metaclass=ABCMeta):
    
    @abstractmethod 
    def save(NewsCollection):
        pass