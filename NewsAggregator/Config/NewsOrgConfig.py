import configparser
from NewsAggregator.IConfig import IConfig

class NewsOrgConfig(IConfig):
    
    __file_name = None
    __base_url = None
    __params = None
    __request_per_day_limit = None

    TYPE_DEFAULT = 'DEFAULT'

    def __init__(self, file_name):
        self.__file_name = file_name
        config = configparser.ConfigParser()
        config.read(self.__file_name)
        self.__base_url = config.get(self.TYPE_DEFAULT, 'url')
        self.__params = config.get(self.TYPE_DEFAULT, 'url_params_list')
        self.__request_per_day_limit = config.get(self.TYPE_DEFAULT, 'request_per_day_limit')

    def get_url(self) -> str:
        return self.__base_url

    def get_params(self) -> str:
        #TODO read params
        return self.__params
 
    def get_request_per_day_limit(self) -> str:
        return self.__request_per_day_limit