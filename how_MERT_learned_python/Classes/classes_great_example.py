# -*- coding: utf-8 -*-
"""   Tue Jun 23 22:09:24 2020   @author: ERTURK
"""


class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model= model
        self.year = year
        self.odometer_reading = 5
    
    def get_descriptive_name(self):
        long_name =str(self.year) + " " +self.make + " "+self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
        
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car("audi","a4", 2016)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()


""" 
We added an atribute self.odometer_reading to the class 
that changes over time. Lets modify it.
"""
my_new_car.odometer_reading=23 # sets it directly.
my_new_car.read_odometer()


"""
We added an function def update_odometer() it will test and change
the value.
"""
my_new_car.odometer_reading=40
my_new_car.update_odometer(3) # we cant roll back an odometer

"""
Now we add new function that will incremently add mileage to the 
odometer_reading and it is called increment_odometer.
"""
my_new_car.increment_odometer(34)
my_new_car.read_odometer()



#####
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " +str(self.battery_size)+ "-kWh battery.")
        
        
    def get_range(self):
        if self.battery_size == 70:
            range =240
        elif self.battery_size == 85:
            range = 270
            
        message ="This car can go approximately " + str(range)
        message +=" miles on full charge."
        print(message)
#####
        
        

""" INHERITENCE """
# The object we are going to add will have the 
# parameters of a default "car" and its own special parameters.

class ElectricCar(Car): # We define child class.
    def __init__(self,make,model,year): 
        super().__init__(make,model,year) #this line puts every "Car" attribute.
                                          #To the "subclass" super. function
                                          #is important because it makes 
                                          # connection between superclass and 
                                          # the childclass.
        
        # We can add any parameter or function that is special to "ElectricCar".
        
        self.battery = Battery() #It will have a battery defined by "class Battery()"
        
    def fill_gas_tank(self): # We can overwrite any method of parentclass in subclass.
        print("Electric cars don't have a gas tank.")

print(" ")

my_tesla = ElectricCar("tesla","model s",2016)

print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

print(" ")


"""
If we find ourself adding too much detail into a class, and figure that we can
write another class we can do that. Now we will add the "class Battery():" 
it will be just before the title 'INHERITENCE'.
"""


my_tesla.battery.describe_battery()
print(" ")
my_tesla.battery.get_range()