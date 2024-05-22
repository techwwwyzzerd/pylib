string = "The quick brown fox jumps over the lazy dog."
keywords = ["fox", "cat", "jumps", "dog", "rabbit"]

result = ""

for word in keywords:
    if word not in string:
        result += word.upper()
    else:
        result += word.lower()
        
print(result)