import requests

class RequestHelper:
    
    @staticmethod
    def get(url):
        return requests.get(url)