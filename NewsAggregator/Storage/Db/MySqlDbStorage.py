
from NewsAggregator.IStorage import IStorage 
from NewsAggregator.Internal.Data.Collection.NewsCollection import NewsCollection

from mysql.connector import MySQLConnection
from datetime import datetime


class MySqlDbStorage(IStorage):

    __instance = None
    __db_name = 'news'
    
    def __new__(cls, __user, __password, __host):
        if cls.__instance is None:
            cls.__instance = super(MySqlDbStorage, cls).__new__(cls)
            cls.__instance.__init_db(__user, __password, __host)
        return cls.__instance

    def __init_db(self, __user, __password, __host):
        self.__user = __user
        self.__password = __password
        self.__host = __host
        self.__connection = MySQLConnection(
            user=self.__user,
            password=self.__password,
            host=self.__host,
            database=self.__db_name
        )

    def create_table(self):
        # TODO update creation of table
        cursor = self.__connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                url TEXT,
                published_at TEXT
            )
        ''')
        self.__connection.commit()
        self.__connection.close()

    def save(self, news_collection: NewsCollection):
        print(news_collection.count())
        current_time = datetime.now()
        if news_collection.count() > 0:
            data = []
            for news_item in news_collection:
                t = (
                    news_item.get_title(), 
                    news_item.get_description(), 
                    news_item.get_url(), 
                    news_item.get_published_at(),
                    news_item.get_author(),
                    news_item.get_url_to_image(),
                    news_item.get_source_id_external(),
                    news_item.get_source_name_external(),
                    news_item.content(),
                    current_time,
                    current_time
                )
                data.append(t)
                query = '''INSERT INTO news (title, description, url, published_at, author,
                url_to_image, source_id_external, source_name_external, content, created, updated) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            
            cursor = self.__connection.cursor()
            cursor.executemany(query, data)
            self.__connection.commit()    
            self.__connection.close()