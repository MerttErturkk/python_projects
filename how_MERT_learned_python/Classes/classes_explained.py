# -*- coding: utf-8 -*-
"""   Tue Jun 23 20:57:05 2020   @author: ERTURK
"""



"""
CLASSES 
"""
class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self,name,age): # self parameter is required in
                                 # the method definition and must
                                 # come before other parameters.
        """initialize name and age attributes."""
        self.name=name
        self.age=age
    
    def sit(self):
        """simulate a dog siting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(self.name.title() + " roll over!")
        
"""
WE must use __init__() in definition because when python calls this
__init__() method later (to create an "instance" of dog),the method call will
automatically passes self,which is a reference  to instance itself; it gives 
the individual instance access to the attributes and methods in the class.
 When we make an instance from the dog class. We'll pass Dog() a name and an 
 age as arguments ; self is passed automatically, so we dont need to pass it.
 Whenever we want to make an instance from the Dog class, we'll provide values
 for only the last two parameters, name and age.
 """
my_dog =Dog("willie",6)
your_dog=Dog("lucy",3)
print("my dogs name is " + my_dog.name.title()+".")
print("my dog is " + str(my_dog.age)+ " years old.")

my_dog.sit() # Dog.sit(my_dog)
my_dog.roll_over() # Dog.roll_over(my_dog)
your_dog.sit()