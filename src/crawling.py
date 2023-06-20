from abc import *
from search_selenium import *


# 0000 0001 : 학위논문  (RISS, NL, NANET)
# 0000 0010 : 학술지    (RISS, NL, NANET)
# 0000 0100 : 도서      (NL, NANET)
# 0000 1000 : 신문      (NL, NANET)
# 0001 0000 : 기사(국내/해외)       (NL, NANET)
# 0010 0000 : 학술논문(국내/해외)   (RISS)

# KOCW는 강의 사이트로 추후 Version 2.0에서 구현할 예정

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
    def CrawlingKOCW(self, crawlingText): pass
    def CrawlingNL(self, crawlingText): pass
    def CrawlingNANET(self, crawlingText): pass 

    def CrawlingRISS(self, crawlingText): 
        seleniumInstance = SingletonSelenium.GetInstance()

        if seleniumInstance.m_driver.window_handles[0] == None: return 
        
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