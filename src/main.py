from login import *
from search import *

if __name__ == "__main__":
    loginLib = SingletonLogin.GetInstance()

    if SingletonLogin.ExistsInstance() == True: 
        searchEInfoCenter = TargetImpl()
        searchEInfoCenter.Serach("RISS", "컴퓨터")