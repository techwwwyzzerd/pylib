def divide_numbers(num,den):
    assert den !=0, "Assertion Error: Division by zero"
    return num / den

try:
    result = divide_numbers(2023,0)
    print (result)
except AssertionError as e:
    print (e)