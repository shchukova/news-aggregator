from abc import ABCMeta, abstractmethod

from NewsAggregator.IScrapper import IScrapper
from NewsAggregator.IParser import IParser
from NewsAggregator.Loader.NewsLoader import NewsLoader


class AbstractNewsLoaderFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_scrapper(self) -> IScrapper:
        pass

    @abstractmethod
    def create_parser(self) -> IParser:
        pass

    @abstractmethod
    def create_loader(self) -> NewsLoader:
        pass