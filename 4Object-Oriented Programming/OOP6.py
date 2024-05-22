# class Init:
#     A=40
#     def __init__(self):
#         print(self.A + self.num1 + self.num2)
        
# obj=Init (4,4)

### working code

class Init:
    A=40
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.A + self.num1 + self.num2)
        
obj=Init (4,4)