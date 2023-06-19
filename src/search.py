import time

from abc import *
from search_selenium import *
from login import *


g_oasis = None

class TargetSearch(ABC): 
    @abstractmethod
    def Search(self, eInfoCenter, searchText): pass

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
        seleniumInstance = SingletonSelenium.GetInstance()

        seleniumInstance.m_driver.find_element('xpath', '//a[@title="RISS"]').click()
        #seleniumInstance.m_driver.get("http://www-riss-kr.openlink.ssu.ac.kr/index.do")
        time.sleep(10) 

        for handle in seleniumInstance.m_driver.window_handles:
            seleniumInstance.m_driver.switch_to.window(handle)
            if handle != seleniumInstance.m_driver.window_handles[0] \
                and seleniumInstance.m_driver.current_url != "http://www-riss-kr.openlink.ssu.ac.kr/index.do":
                    seleniumInstance.m_driver.switch_to.window(handle)
                    seleniumInstance.m_driver.close()

        seleniumInstance.m_driver.switch_to.window(seleniumInstance.m_driver.window_handles[-1])
        seleniumInstance.m_driver.find_element('id', 'query').send_keys(searchText)
        seleniumInstance.m_driver.find_element('css selector', '.btnSearch').click()
        time.sleep(3)

class SearchEInfoCenterKOCW(AdvancedEInfoCenterSearch):
    def SearchRISS(self, searchText): pass
    def SearchNL(self, searchText): pass
    def SearchNANET(self, searchText): pass 

    def SearchKOCW(self, searchText):
        seleniumInstance = SingletonSelenium.GetInstance()

        seleniumInstance.m_driver.find_element('xpath', '//a[@title="KOCW"]').click()
        #seleniumInstance.m_driver.get("http://www.kocw.net/home/index.do")
        time.sleep(10) 

        for handle in seleniumInstance.m_driver.window_handles:
            seleniumInstance.m_driver.switch_to.window(handle)
            if handle != seleniumInstance.m_driver.window_handles[0] \
                and seleniumInstance.m_driver.current_url != "http://www.kocw.net/home/index.do":
                    seleniumInstance.m_driver.switch_to.window(handle)
                    seleniumInstance.m_driver.close()    

        seleniumInstance.m_driver.switch_to.window(seleniumInstance.m_driver.window_handles[-1])
        seleniumInstance.m_driver.find_element('id', 'query').send_keys(searchText)
        seleniumInstance.m_driver.find_element('css selector', '.searchBtn').click()
        time.sleep(3)

class SearchEInfoCenterNL(AdvancedEInfoCenterSearch):
    def SearchRISS(self, searchText): pass
    def SearchKOCW(self, searchText): pass
    def SearchNANET(self, searchText): pass 

    def SearchNL(self, searchText):
        seleniumInstance = SingletonSelenium.GetInstance()

        seleniumInstance.m_driver.find_element('xpath', '//a[@title="국립중앙도서관"]').click()
        #seleniumInstance.m_driver.get("https://www.nl.go.kr")
        time.sleep(10) 

        seleniumInstance.m_driver.switch_to.window(seleniumInstance.m_driver.window_handles[-1])
        seleniumInstance.m_driver.find_element('id', 'main_input-text1').send_keys(searchText)
        seleniumInstance.m_driver.find_element('css selector', '.btn-search').click()
        time.sleep(3)

class SearchEInfoCenterNANET(AdvancedEInfoCenterSearch):
    def SearchRISS(self, searchText): pass
    def SearchKOCW(self, searchText): pass
    def SearchNL(self, searchText): pass 

    def SearchNANET(self, searchText):
        seleniumInstance = SingletonSelenium.GetInstance()

        seleniumInstance.m_driver.find_element('xpath', '//a[@title="국회도서관"]').click()
        #seleniumInstance.m_driver.get("https://www.nanet.go.kr/main.do")
        time.sleep(10) 

        seleniumInstance.m_driver.switch_to.window(seleniumInstance.m_driver.window_handles[-1])
        seleniumInstance.m_driver.find_element('id', 'query').send_keys(searchText)
        seleniumInstance.m_driver.find_element('id', 'elecSearch').send_keys(searchText)
        time.sleep(3)

class AdapterSearch(TargetSearch):
    def __init__(self, eInfoCenter):
        global g_oasis

        loginInstance = SingletonLogin.GetInstance()
        seleniumInstance = SingletonSelenium.GetInstance()

        if loginInstance.ExistsInstance() != True \
            and seleniumInstance.ExistsInstance() != True : return
        
        if g_oasis == None:
            seleniumInstance.m_driver.get("https://oasis.ssu.ac.kr/")
            
            seleniumInstance.m_driver.find_element('id', 'goto-login').click()
            seleniumInstance.m_driver.find_element('id', 'userid').send_keys(loginInstance.m_id)
            seleniumInstance.m_driver.find_element('id', 'password').send_keys(loginInstance.m_pw)
            seleniumInstance.m_driver.find_element('css selector', '.btn-block[type="submit"]').click()

            g_oasis = seleniumInstance.m_driver.current_window_handle

        seleniumInstance.m_driver.switch_to.window(g_oasis)
        time.sleep(3)

        if eInfoCenter == "RISS": self.advancedEInfoCenter = SearchEInfoCenterRISS()
        elif eInfoCenter == "KOCW": self.advancedEInfoCenter = SearchEInfoCenterKOCW()
        elif eInfoCenter == "NL": self.advancedEInfoCenter = SearchEInfoCenterNL()
        elif eInfoCenter == "NANET": self.advancedEInfoCenter = SearchEInfoCenterNANET()

    def Search(self, eInfoCenter, searchText):
        if eInfoCenter == "RISS": self.advancedEInfoCenter.SearchRISS(searchText)
        elif eInfoCenter == "KOCW": self.advancedEInfoCenter.SearchKOCW(searchText)
        elif eInfoCenter == "NL": self.advancedEInfoCenter.SearchNL(searchText)
        elif eInfoCenter == "NANET": self.advancedEInfoCenter.SearchNANET(searchText)

class TargetSearchImpl(TargetSearch):
    def __init__(self): self.adapter = None
    
    def Search(self, eInfoCenter, searchText):
        self.adapter = AdapterSearch(eInfoCenter)
        self.adapter.Search(eInfoCenter, searchText)
    




