from login import *
from search import *


if __name__ == "__main__":
    loginLib = SingletonLogin.GetInstance()
    searchEInfoCenter = None

    if loginLib.ExistsInstance() == True: 
        searchEInfoCenter = TargetImpl()
        searchEInfoCenter.Serach("RISS", "test")
        searchEInfoCenter.Serach("KOCW", "test")
        searchEInfoCenter.Serach("NL", "test")
        searchEInfoCenter.Serach("NANET", "test")