# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:01:58 2020

@author: ERTURK
"""

class Matematik:
    def __init__(self):
        print("çalıştı")
        
        
    def topla(self,sayı1,sayı2):
        return sayı1+sayı2
    
    def çıkar(self,sayı1,sayı2):
        return (sayı1-sayı2)
    
    def çarp (self,sayı1,sayı2):
        return sayı1*sayı2
    
    def böl(self,sayı1,sayı2):
        return (sayı1/sayı2)
    
    
matematik=Matematik()
matematik2=Matematik()


print("toplam = " +str(matematik.topla(2,78)))

####################################3


class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age



person1=Person("mert", "erturk", 22)
print(person1.age)


class worker(Person):                                   # PERSONDAN INHERITANCE ALIYO YANİ MİRAS
    def __init__(self,firstname,lastname,age,salary):   # PERSONIN SAHİP OLDUĞU TÜM ÖZELLİKLERER SAHİP
        super().__init__(firstname,lastname,age)   
        self.salary= salary
        
class customer(Person):
    def __init__(self,firstname,lastname,age,creditcardnumber):
        super().__init__(firstname,lastname,age) 
        self.creditcardnumber=creditcardnumber
        
ahmet=worker("ahmet","mehmet",32,599)
print(ahmet.salary)
mehmet=customer("ali","veli",33,515125555222)
mehmet.creditcardnumber = 5122233333