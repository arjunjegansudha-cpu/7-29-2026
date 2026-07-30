class vehicle:
    def __init__ (self,max_speed,mileage,color):
        self.max_speed=max_speed
        self.mileage=mileage
        self.color=color
BMW=vehicle(230,20,'black')
tesla=vehicle(180,13,'blue')
print('The max speed of BMW is:',BMW.max_speed)
print('The mileage of BMW is:',BMW.mileage)
print('The color of the BMW is:',BMW.color)
print('')
print('The max speed of Tesla is:',tesla.max_speed)
print('The mileage of Tesla is:',tesla.mileage)
print('The color of the tesla is:',tesla.color)