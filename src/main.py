from login import *
#from search import *
from context import *


if __name__ == "__main__":
    loginInstance = SingletonLogin.GetInstance("20231673", "1qazxsw2!@")
    context = None

    if loginInstance.ExistsInstance() == True: 
        context = SingletonContext.GetInstance()
        context.facadeContext.SearchAndCrawl("RISS", "test")
        context.facadeContext.SearchAndCrawl("KOCW", "test")
        context.facadeContext.SearchAndCrawl("NL", "test")
        context.facadeContext.SearchAndCrawl("NANET", "test")