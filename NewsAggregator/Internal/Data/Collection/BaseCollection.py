from NewsAggregator.Internal.Data.ICollection import ICollection
from NewsAggregator.Internal.Data.IItem import IItem

class BaseCollection(ICollection):
    
    def __init__(self, data = []):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

    def add_items(items: dict):
        for item in items:
            self.append_item(item)

    def append_item(self, item: IItem):
        self.data.append(item)
    
    def count(self):
        return len(self.data)