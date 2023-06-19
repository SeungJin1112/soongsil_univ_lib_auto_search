from login import *
from search import *


if __name__ == "__main__":
    loginInstance = SingletonLogin.GetInstance("input id", "input pw")
    searchEInfoCenter = None

    if loginInstance.ExistsInstance() == True: 
        searchEInfoCenter = TargetImpl()
        searchEInfoCenter.Search("RISS", "test")
        searchEInfoCenter.Search("KOCW", "test")
        searchEInfoCenter.Search("NL", "test")
        searchEInfoCenter.Search("NANET", "test")