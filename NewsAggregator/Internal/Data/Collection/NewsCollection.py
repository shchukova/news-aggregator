from NewsAggregator.Internal.Data.ICollection import ICollection
from NewsAggregator.Internal.Data.IItem import IItem
from NewsAggregator.Internal.Data.Item.NewsItem import NewsItem 
from NewsAggregator.Internal.Data.Collection.BaseCollection import BaseCollection


class NewsCollection(BaseCollection):

    def __ensueItem(item: IItem):
        #TODO check type of the item
        return true

    def __create_item_from_dict(data: dict) -> NewsItem:
        return NewsItem.create_from_dict(data)