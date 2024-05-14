class CustomException(Exception):
    def __init__ (self,arg):
        self._arg = arg
    @property
    def arg(self):
        return self._arg
    
try:
    raise CustomException(56)
except CustomException as e:
    print(e.arg)