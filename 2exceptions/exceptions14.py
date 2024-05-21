class NegativeValueException (Exception):
    def __init__ (self, message):
        self.message = message
        
    def __str__ (self): 
        return f"NegativeValueException: {self.message}"
    
def process_data(data):
    try:
        if data < 0:
            raise NegativeValueException("Negative value not allowed")
        else:
            return data * 2
    except ValueError as e:
        return str(e)
    except NegativeValueException as e:
        return str(e)
    
print (process_data (-3))