from NewsAggregator.Internal.Data.IItem import IItem
from NewsAggregator.Internal.Data.Item.BaseItem import BaseItem

class NewsItem(BaseItem):
    _source_name_external = None
    _source_id_external = None
    _author = None
    _title = None
    _description = None
    _url = None
    _url_to_image = None
    _published_at = None
    _content = None
    _url_to_image = None

    def __init__(self, _title: str, _url: str, data: dict):
        self._title = _title
        self._url = _url
        self._source_id_external = data['source_id_external']
        self._source_name_external = data['source_name_external']
        self._description = data['description']
        self._url_to_image = data['url_to_image']
        self._published_at = data['published']
        self._content = data['content']
        self._author = data['author']
        self._url_to_image = data['url_to_image']

    @staticmethod
    def create_from_dict(self, data: dict):
        return NewsItem(data['title'], data['url'], data)

    def get_id(self) -> int:
        #TODO unique id
        return IItem.TYPE_NEWS

    def get_name(self) -> str:
        return 'news_item'

    def get_type(self) -> int:
        return IItem.TYPE_NEWS

    def get_title(self) -> str:
        return self._title

    def get_published_at(self) -> str:
        return self._published_at
    
    def get_content(self) -> str:
        return self._content

    def get_author(self) -> str:
        return self._author

    def get_description(self) -> str:
        return self._description

    def get_url(self) -> str:
        return self._url
    
    def get_url_to_image(self) -> str:
        return self._url_to_image
    
    def get_source_id_external(self) -> str:
        return self._source_id_external
    
    def get_source_name_external(self) -> str:
        return self._source_name_external





















