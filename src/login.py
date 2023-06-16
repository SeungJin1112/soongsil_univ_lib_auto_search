class SingletonLogin:
    _instance = None

    def __init__(self):
        if SingletonLogin._instance != None: 
            raise Exception("ERROR(CLASS: SingletonLogin, MSG: instance already exists)")
        else: SingletonLogin._instance = self

    def GetInstance():
        if SingletonLogin._instance == None: SingletonLogin()

        return SingletonLogin._instance
    
    def ExistsInstance(cls):
        if SingletonLogin._instance == None: return False
        else : return True

    