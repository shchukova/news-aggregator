from NewsAggregator.Loader.NewsLoader import NewsLoader
from NewsAggregator.IStorage import IStorage
from NewsAggregator.ILoader import ILoader

class NewsAggregator:

    __news_loader_list: list[ILoader] = None

    def __init__(self, __storage: IStorage):
        self.__storage = __storage
        self.__news_loader_list = []

    def add(self, news_loader: ILoader):
        self.__news_loader_list.append(news_loader)

    def run(self):
        for loader in self.__news_loader_list:
            news_collection = loader.get_news_collection()
            if news_collection is not None and news_collection.count() > 0:
                self.__storage.save(news_collection)
