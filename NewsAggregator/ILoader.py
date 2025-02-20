from abc import ABCMeta, abstractmethod

class ILoader(metaclass=ABCMeta):
    
    @abstractmethod 
    def get_news_collection():
        pass