string = "Python"
multiplier = 3
result = ""

for i in range (len(string)):
    if i % 2 == 0:
        result += string [i] * multiplier
    else: result += string[i]
    
result = result[::-1]
print(result)