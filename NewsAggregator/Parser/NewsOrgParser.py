from NewsAggregator.IParser import IParser
from NewsAggregator.Internal.Data.Collection.NewsCollection import NewsCollection
from NewsAggregator.Internal.Data.Item.PageContent import PageContent
from NewsAggregator.Internal.Data.Item.NewsItem import NewsItem
import json

class NewsOrgParser(IParser):

    FIELD_STATUS = 'status'
    RESPONSE_STATUS_OK = 'ok'
    FIELD_TOTAL = 'totalResults'
    FIELD_NEWS = 'articles'
    FIELD_SOURCE = 'source'
    FIELD_SOURCE_ID = 'id'
    FIELD_SOURCE_NAME = 'name'
    FIELD_AUTHOR = 'author'
    FIELD_TITLE = 'title'
    FIELD_DESCRIPTION = 'description'
    FIELD_URL = 'url'
    FIELD_URL_TO_IMAGE = 'urlToImage'
    FIELD_PUBLISHED_AT = 'publishedAt'
    FIELD_CONTENT = 'content'

    def parse(self, page: PageContent) -> NewsCollection:
        json_string = page.get_content().text
        data = json.loads(json_string)
        news_collection = NewsCollection()
        if data.get(self.FIELD_STATUS) is not None:
            if data[self.FIELD_STATUS] == self.RESPONSE_STATUS_OK:
                if data.get(self.FIELD_NEWS) is not None:
                    articles = data[self.FIELD_NEWS]
                    sourceInfo = self._get_source_info(data)
                    for article in articles:
                        articleInfo = self._get_article_info(article)
                        news_item = NewsItem(_title=article['title'], _url=article['url'], data=articleInfo)
                        news_collection.append_item(news_item)

        return news_collection

    def _get_source_info(self, data) -> dict:
        result = {
            'external_source_name': None, 
            'external_source_id': None
        }
        if data.get(self.FIELD_SOURCE) is not None:
            source = data[self.FIELD_SOURCE]
            if source.get(self.FIELD_SOURCE_ID) is not None:
                result['external_source_id'] = source[self.FIELD_SOURCE_ID]
            if source.get(self.FIELD_SOURCE_NAME) is not None:
                result['external_source_name'] = source[self.FIELD_SOURCE_NAME]
    
        return result

    def _get_article_info(self, data) -> dict:
        source = self._get_source_info(data)
        result = {
            'external_source_name': source['external_source_name'],
            'external_source_id': source['external_source_id'],
            'published': '',
            'url': '',
            'url_to_image': '',
            'title': '',
            'description': '',
            'content': '',
            'author': ''
        }
        if data.get(self.FIELD_TITLE) is not None:
            result[self.FIELD_TITLE] = data[self.FIELD_TITLE]
        if data.get(self.FIELD_AUTHOR) is not None:
            result[self.FIELD_AUTHOR] = data[self.FIELD_AUTHOR]
        if data.get(self.FIELD_PUBLISHED_AT) is not None:
            result[self.FIELD_PUBLISHED_AT] = data[self.FIELD_PUBLISHED_AT]
        if data.get(self.FIELD_CONTENT) is not None:
            result[self.FIELD_CONTENT] = data[self.FIELD_CONTENT]
        if data.get(self.FIELD_DESCRIPTION) is not None:
            result[self.FIELD_DESCRIPTION] = data[self.FIELD_DESCRIPTION]
        if data.get(self.FIELD_URL) is not None:
            result[self.FIELD_URL] = data[self.FIELD_URL]
        if data.get(self.FIELD_URL_TO_IMAGE) is not None:
            result[self.FIELD_URL_TO_IMAGE] = data[self.FIELD_URL_TO_IMAGE]
        return result