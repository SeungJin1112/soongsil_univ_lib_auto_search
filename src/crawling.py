from abc import *


class TargetCrawling(ABC): 
    @abstractmethod
    def Crawling(self, eInfoCenter, crawlingText): pass

class AdvancedEInfoCenterCrawling(ABC):
    @abstractmethod
    def CrawlingRISS(self, crawlingText): pass
    def CrawlingKOCW(self, crawlingText): pass
    def CrawlingNL(self, crawlingText): pass
    def CrawlingNANET(self, crawlingText): pass 

class CrawlingEInfoCenterRISS(AdvancedEInfoCenterCrawling):
    def CrawlingRISS(self, crawlingText): pass
    def CrawlingKOCW(self, crawlingText): pass
    def CrawlingNL(self, crawlingText): pass
    def CrawlingNANET(self, crawlingText): pass 

class CrawlingEInfoCenterKOCW(AdvancedEInfoCenterCrawling):
    def CrawlingRISS(self, crawlingText): pass
    def CrawlingKOCW(self, crawlingText): pass
    def CrawlingNL(self, crawlingText): pass
    def CrawlingNANET(self, crawlingText): pass 

class CrawlingEInfoCenterNL(AdvancedEInfoCenterCrawling):
    def CrawlingRISS(self, crawlingText): pass
    def CrawlingKOCW(self, crawlingText): pass
    def CrawlingNL(self, crawlingText): pass
    def CrawlingNANET(self, crawlingText): pass 

class CrawlingEInfoCenterNANET(AdvancedEInfoCenterCrawling):
    def CrawlingRISS(self, crawlingText): pass
    def CrawlingKOCW(self, crawlingText): pass
    def CrawlingNL(self, crawlingText): pass
    def CrawlingNANET(self, crawlingText): pass 

class AdapterCrawling(TargetCrawling):
    def __init__(self, eInfoCenter):         
        if eInfoCenter == "RISS": self.advancedEInfoCenter = CrawlingEInfoCenterRISS()
        elif eInfoCenter == "KOCW": self.advancedEInfoCenter = CrawlingEInfoCenterKOCW()
        elif eInfoCenter == "NL": self.advancedEInfoCenter = CrawlingEInfoCenterNL()
        elif eInfoCenter == "NANET": self.advancedEInfoCenter = CrawlingEInfoCenterNANET()

    def Crawling(self, eInfoCenter, crawlingText):
        if eInfoCenter == "RISS": self.advancedEInfoCenter.CrawlingRISS(crawlingText)
        elif eInfoCenter == "KOCW": self.advancedEInfoCenter.CrawlingKOCW(crawlingText)
        elif eInfoCenter == "NL": self.advancedEInfoCenter.CrawlingNL(crawlingText)
        elif eInfoCenter == "NANET": self.advancedEInfoCenter.CrawlingNANET(crawlingText)

class TargetCrawlingImpl(TargetCrawling):
    def __init__(self): self.adapter = None
    
    def Crawling(self, eInfoCenter, crawlingText):
        self.adapter = AdapterCrawling(eInfoCenter)
        self.adapter.Crawling(eInfoCenter, crawlingText)