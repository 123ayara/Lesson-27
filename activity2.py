class vehicles:
    def __init__(self,speed,milage):
        self.speed=speed
        self.milage=milage
obj=vehicles(100,10)
model=vehicles(110, 10)
print(obj.speed)
print(model.milage)
print(obj.milage)
print(model.speed)