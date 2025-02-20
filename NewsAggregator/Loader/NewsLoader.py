
from NewsAggregator.IScrapper import IScrapper
from NewsAggregator.IParser import IParser
from NewsAggregator.Internal.Data.Collection.NewsCollection import NewsCollection

class NewsLoader():

    __worker: IScrapper = None
    __parser: IParser = None

    def __init__(self, __worker: IScrapper, __parser: IParser):
        self.__worker = __worker
        self.__parser = __parser

    def get_worker(self) -> IScrapper:
        return self.__worker

    def get_parser(self) -> IParser:
        return self.__parser

    def get_news_collection(self) -> NewsCollection:
        response = self.get_worker().get_data(self.get_worker().get_requested_url())
        news_collection = self.get_parser().parse(response)
        return news_collection