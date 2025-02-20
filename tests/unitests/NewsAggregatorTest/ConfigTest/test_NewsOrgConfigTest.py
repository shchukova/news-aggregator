import unittest

from ....NewsAggregator.Config.NewsOrgConfig import NewsOrgConfig

class test_NewsOrgConfigTest(unittest.TestCase):

    __testFile = 'newsorg_config_test.ini'

    def test_get_url(self):
        config = NewsOrgConfig(self.__testFile)
        result = config.get_url()
        self.assertEqual(result, 'https://newsapi.org/v2')

    def test_get_params(self):
        config = NewsOrgConfig(self.__testFile)
        result = config.get_params()
        self.assertEqual(result, 'apiKey={APIKEY}&country={COUNTRY}&from={FROM}&to={TO}')
    
    def test_get_request_per_day_limit(self):
        config = NewsOrgConfig(self.__testFile)
        result = config.get_request_per_day_limit()
        self.assertEqual(result, '5')