from abc import *

from selenium import webdriver
import chromedriver_autoinstaller

class TargetSelenium(ABC):
    @abstractmethod
    def Serach(): pass
    def Get(): pass

class AdvancedSelenium(ABC):
    @abstractmethod
    def GetInstance(): pass