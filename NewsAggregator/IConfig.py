from abc import ABCMeta, abstractmethod

class IConfig(metaclass=ABCMeta):

    @abstractmethod 
    def get_url() -> str:
        pass

    @abstractmethod 
    def get_params() -> str:
        pass

    @abstractmethod 
    def get_request_per_day_limit() -> str:
        pass