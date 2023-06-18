from login import *
from search import *


if __name__ == "__main__":
    loginInstance = SingletonLogin.GetInstance("input id", "input pw")
    searchEInfoCenter = None

    if loginInstance.ExistsInstance() == True: 
        searchEInfoCenter = TargetImpl()
        searchEInfoCenter.Serach("RISS", "test")
        searchEInfoCenter.Serach("KOCW", "test")
        searchEInfoCenter.Serach("NL", "test")
        searchEInfoCenter.Serach("NANET", "test")