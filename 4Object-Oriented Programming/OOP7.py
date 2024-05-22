class CarF1:
    speed=275
    def __init__ (self,var1,var2,var3,var4):
        self.name=var1
        self.HorsePower=var2
        self.color=var3
        CarF1.speed =var4
        
car=CarF1("Ferrari",1000,"red",300)
print(car.__dict__)