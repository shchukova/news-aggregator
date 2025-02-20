from abc import ABCMeta, abstractmethod

class IItem(metaclass=ABCMeta):
    
    TYPE_NEWS = 1

    @abstractmethod
    def get_id() -> int:
        pass
    
    @abstractmethod 
    def get_name() -> str:
        pass