from abc import *
from search_selenium import *
from login import *


class TargetSearch(ABC): 
    @abstractmethod
    def Serach(self, eInfoCenter, searchText): pass

class AdvancedEInfoCenterSearch(ABC):
    @abstractmethod
    def SearchRISS(self, searchText): pass
    def SearchKOCW(self, searchText): pass
    def SearchNL(self, searchText): pass
    def SearchNANET(self, searchText): pass 

class SearchEInfoCenterRISS(AdvancedEInfoCenterSearch):
    def SearchKOCW(self, searchText): pass
    def SearchNL(self, searchText): pass
    def SearchNANET(self, searchText): pass 

    def SearchRISS(self, searchText):
        seleniumLib = SingletonSelenium.GetInstance()
        seleniumLib.driver.get("http://www-riss-kr.openlink.ssu.ac.kr/index.do")

class SearchEInfoCenterKOCW(AdvancedEInfoCenterSearch):
    def SearchRISS(self, searchText): pass
    def SearchNL(self, searchText): pass
    def SearchNANET(self, searchText): pass 

    def SearchKOCW(self, searchText):
        seleniumLib = SingletonSelenium.GetInstance()
        seleniumLib.driver.get("http://www.kocw.net/home/index.do")

class SearchEInfoCenterNL(AdvancedEInfoCenterSearch):
    def SearchRISS(self, searchText): pass
    def SearchKOCW(self, searchText): pass
    def SearchNANET(self, searchText): pass 

    def SearchNL(self, searchText):
        seleniumLib = SingletonSelenium.GetInstance()
        seleniumLib.driver.get("https://www.nl.go.kr/")

class SearchEInfoCenterNANET(AdvancedEInfoCenterSearch):
    def SearchRISS(self, searchText): pass
    def SearchKOCW(self, searchText): pass
    def SearchNL(self, searchText): pass 

    def SearchNANET(self, searchText):
        seleniumLib = SingletonSelenium.GetInstance()
        seleniumLib.driver.get("https://www.nanet.go.kr/main.do")

class AdapterSearch(TargetSearch):
    def __init__(self, eInfoCenter):
        if eInfoCenter == "RISS": self.advancedEInfoCenter = SearchEInfoCenterRISS()
        elif eInfoCenter == "KOCW": self.advancedEInfoCenter = SearchEInfoCenterKOCW()
        elif eInfoCenter == "NL": self.advancedEInfoCenter = SearchEInfoCenterNL()
        elif eInfoCenter == "NANET": self.advancedEInfoCenter = SearchEInfoCenterNANET()

    def Serach(self, eInfoCenter, searchText):
        if eInfoCenter == "RISS": self.advancedEInfoCenter.SearchRISS(searchText)
        elif eInfoCenter == "KOCW": self.advancedEInfoCenter.SearchKOCW(searchText)
        elif eInfoCenter == "NL": self.advancedEInfoCenter.SearchNL(searchText)
        elif eInfoCenter == "NANET": self.advancedEInfoCenter.SearchNANET(searchText)

class TargetImpl(TargetSearch):
    def __init__(self): self.adapter = None
    
    def Serach(self, eInfoCenter, searchText):
        self.adapter = AdapterSearch(eInfoCenter)
        self.adapter.Serach(eInfoCenter, searchText)
    




