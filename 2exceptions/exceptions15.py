class DataFormatException(Exception):
    def __init__(self,message,data):
        self.message = message
        self.data = data
    
    def __str__(self):
        return f"DataFormatException: {self.message}, Data: {self.data}"
    
class CustomException (Exception):
    def __init__(self,message):
        self.message = message
        
    def __str__ (self):
        return f"CustomException: {self.message}"
def process_data(data):
    try:
        if not isinstance(data,str):
            raise DataFormatException("Invalid data format", data)
        elif len(data) < 5:
            raise CustomException ("Data lenght is too short")
        elif len(data) > 10:
            raise CustomException ("Data length is too long")
        else:
            return data.upper()
    except DataFormatException as e:
        return str(e)
    except CustomException as e:
        return str(e)
    
print (process_data(12345))