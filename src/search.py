from abc import *
from search_selenium import *

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
    def SearchRISS(self, searchText):
        print(f"RISS : {searchText}")

class SearchEInfoCenterKOCW(AdvancedEInfoCenterSearch):
    def SearchKOCW(self, searchText):
        print(f"KOCW : {searchText}")

class SearchEInfoCenterNL(AdvancedEInfoCenterSearch):
    def SearchNL(self, searchText):
        print(f"NL : {searchText}")

class SearchEInfoCenterNANET(AdvancedEInfoCenterSearch):
    def SearchNANET(self, searchText):
        print(f"NANET : {searchText}")

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
    




