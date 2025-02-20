from NewsAggregator.Helper.RequestHelper import RequestHelper
from NewsAggregator.IScrapper import IScrapper
from NewsAggregator.IConfig import IConfig
from NewsAggregator.Internal.Data.Item.PageContent import PageContent 

class NewsOrgApiScrapper(IScrapper):

    _config: IConfig = None

    def __init__(self, config: IConfig):
        self.__config = config

    def get_config(self) -> IConfig:
        return self.__config

    def get_data(self, url: str) -> PageContent:
        r = RequestHelper.get(url)
        response = PageContent(url, r)
        return response

    def _convert_params_to_str(self, params) -> str:
        ##TODO
        return ''

    def get_requested_url(self) -> str:
        #TODO
        #paramsToStr = self._convert_params_to_str(self.get_config().get_params())
        url = self.get_config().get_url()
        return url