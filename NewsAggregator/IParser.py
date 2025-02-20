from abc import ABCMeta, abstractmethod
from NewsAggregator.Internal.Data.Item.PageContent import PageContent 
from NewsAggregator.Internal.Data.Collection.NewsCollection import NewsCollection

class IParser(metaclass=ABCMeta):
    
    @abstractmethod 
    def parse(self, page: PageContent) -> NewsCollection:
        pass