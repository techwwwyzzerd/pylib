class MySpecificException (Exception):
    pass
def divide_two_numbers (number1,number2):
    if number2== 0:
        raise MySpecificException("Cannot divide by zero")
    return number1/number2

try:
    result = divide_two_numbers(22,0)
    print (result)
except ValueError as v:
    print ("this is a values error")
except SyntaxError as s:
    print (s)
except MySpecificException as e:
    print (e)