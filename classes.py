import constants as DZ
import inspect
import pprint

class MyNewClass:
    '''Docstring here ...'''
    # local namespace 
    pass

class User:
    '''User docstring'''
    age = 10
    
    def greet(self):
        print('hello there')
        
# Output: 10
DZ.LINE(User.age)
DZ.LINE(User.greet)
DZ.LINE(User.__doc__)

dueminalov = User()

DZ.LINE(dueminalov.greet())

class api_SmartSheet:
    '''Connection to SmartSheet and it's API endpoints'''
    __dbPdo = '-connection to sql-'
    __logErr = "-E_ALL-"
    __steUser = '0xb5589228'
    __auditLog = []
    __pp = pprint.PrettyPrinter(indent=4)
    
    def __init__(self):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.__auditLog.append(str(calframe[1][4][-1]).strip())
    
    def sync_sheets(self):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.__auditLog.append(str(calframe[1][4][-1]).strip())
    
    def process_newSheet(self):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.__auditLog.append(str(calframe[1][4][-1]).strip())
    
    def audit(self):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        self.__auditLog.append(str(calframe[1][4][-1]).strip())
        self.__pp.pprint(self.__auditLog)
        
    
SmartSheet = api_SmartSheet()
#SmartSheet.__auditLog.append('test') # __ is private attribute
SmartSheet.sync_sheets()
SmartSheet.audit()