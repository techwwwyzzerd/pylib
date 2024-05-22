def manipulate_string(s):
    s = s [::-1]
    s += "!"
    return s
text = "Python"
modified_text = manipulate_string(text)
print (modified_text)