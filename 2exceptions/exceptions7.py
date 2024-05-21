try:
    #Code block 1
    raise ValueError ("Error 1")
except ValueError as e1:
    # Code block 2
    raise TypeError("Error 2") from e1
except:
    # Code Block 3
    raise RuntimeError("Error 3")
else:
    # Code Block 4
    raise NameError("Error 4")
finally:
    # Code Block 5
    print("Finally block")