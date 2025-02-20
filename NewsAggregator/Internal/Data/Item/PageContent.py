class PageContent:

    __requested_url = None
    __content = None

    def __init__(self, url, content):
        self.__requested_url = url
        self.__content = content

    @staticmethod
    def create_from_array(self):
        pass
    
    def get_content(self):
        return self.__content

    def get_requested_url(self):
        return self.__requested_url
