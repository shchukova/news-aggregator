from NewsAggregator.Config.NewsOrgConfig import NewsOrgConfig
from NewsAggregator.Scrapper.NewsOrgApiScrapper import NewsOrgApiScrapper
from NewsAggregator.Parser.NewsOrgParser import NewsOrgParser
from NewsAggregator.Storage.Db.MySqlDbStorage import MySqlDbStorage
from NewsAggregator.NewsAggregator import NewsAggregator
from NewsAggregator.Loader.NewsLoader import NewsLoader

import os
from dotenv import load_dotenv

if __name__ == '__main__':

    load_dotenv()
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASS = os.environ['MYSQL_PASS']
    MYSQL_HOST = os.environ['MYSQL_HOST']

    config = NewsOrgConfig('./config/newsorg_config.ini')

    storage = MySqlDbStorage(MYSQL_USER, MYSQL_PASS, MYSQL_HOST)
    scrapper = NewsOrgApiScrapper(config)
    

    parser = NewsOrgParser()


    news_loader = NewsLoader(scrapper, parser)
    news_aggregator = NewsAggregator(storage)
    news_aggregator.add(news_loader)
    news_aggregator.run()