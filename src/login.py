class SingletonLogin:
    _instance = None

    def __init__(self):
        if SingletonLogin._instance != None: raise Exception("ERROR: instance already exists")
        else: SingletonLogin._instance = self

    def GetInstance():
        if SingletonLogin._instance == None: SingletonLogin()

        return SingletonLogin._instance
    
    def ExistsInstance():
        if SingletonLogin._instance == None: return False
        else : return True

    