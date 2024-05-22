def modify_string(s):
    s[0] = 'M'
    return s

message = "Hello"
new_message = modify_string (message)
print(new_message)