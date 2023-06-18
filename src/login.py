class SingletonLogin:
    _instance = None

    def __init__(self, id, pw):
        if SingletonLogin._instance != None: 
            raise Exception("ERROR(CLASS: SingletonLogin, MSG: instance already exists)")
        
        SingletonLogin._instance = self
        self.m_id = id
        self.m_pw = pw

    def GetInstance(id=None, pw=None):
        if id != None and pw != None: 
            if SingletonLogin._instance == None: 
                SingletonLogin(id, pw)

        return SingletonLogin._instance
    
    def ExistsInstance(cls):
        if SingletonLogin._instance == None: return False
        else : return True

    