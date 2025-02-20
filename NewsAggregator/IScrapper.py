from abc import ABCMeta, abstractmethod
from NewsAggregator.Internal.Data.Item.PageContent import PageContent

class IScrapper(metaclass=ABCMeta):

    @abstractmethod 
    def get_data(url: str) -> PageContent:
        pass

    @abstractmethod 
    def get_requested_url() -> str:
        pass