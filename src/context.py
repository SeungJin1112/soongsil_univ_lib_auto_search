from search import *
from crawling import *


class FacadeContext:
    def __init__(self):
        self.searchService = TargetSearchImpl()
        self.crawlingService = TargetCrawlingImpl()

    def SearchAndCrawl(self, eInfoCenter, text):
        self.searchService.Search(eInfoCenter, text)
        self.crawlingService.Crawling(eInfoCenter, text)

class SingletonContext:
    _instance = None

    def __init__(self):
        if SingletonSelenium._instance != None: 
            raise Exception("ERROR(CLASS: SingletonContext, MSG: instance already exists)")
        
        SingletonContext._instance = self
        self.facadeContext = FacadeContext()

    def GetInstance():
        if SingletonContext._instance == None: SingletonContext()

        return SingletonContext._instance

    def ExistsInstance(cls):
        if SingletonContext._instance == None: return False
        else : return True