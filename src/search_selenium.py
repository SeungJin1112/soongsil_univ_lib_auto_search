from chromedriver_autoinstaller import install as install_chromedriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


class SingletonSelenium:
    _instance = None

    def __init__(self):
        if SingletonSelenium._instance != None: 
            raise Exception("ERROR(CLASS: SingletonSelenium, MSG: instance already exists)")
        
        SingletonSelenium._instance = self
        install_chromedriver()

        self.m_chromeOptions = Options()
        #chromeOptions.add_argument('--headless')

        self.m_driver = webdriver.Chrome(service=Service(), options=self.m_chromeOptions)
            
    def GetInstance():
        if SingletonSelenium._instance == None: SingletonSelenium()

        return SingletonSelenium._instance
    
    
    def ExistsInstance(cls):
        if SingletonSelenium._instance == None: return False
        else : return True

    def CloseDriver(self):
        if self.m_driver:
            self.m_driver.quit()
            self.m_driver = None