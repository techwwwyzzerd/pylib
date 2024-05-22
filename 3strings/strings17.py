string = "Prasoon"
number = 5
result = ""

for i in range (len(string)):
    result += chr(ord(string[i]) + number)
    
result = result [::-1]
print(result)