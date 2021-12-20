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