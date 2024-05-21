def process_string(string):
    try:
        length = len(string)
        first_char = string [1]
        last_char = string [-1]
        converted_int = int(string)
    except IndexError:
        return "Empty String"
    except ValueError:
        return "Invalid integer conversion"
    else:
        return length, first_char, last_char
print (process_string("Hello"))
print (process_string("7890"))