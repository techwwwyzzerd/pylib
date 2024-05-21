try:
    raise ValueError("Wrong code", 258)
except ValueError as err:
    print("Arguments:", err.args)