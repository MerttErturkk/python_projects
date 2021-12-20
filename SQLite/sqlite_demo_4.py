# -*- coding: utf-8 -*-

import sqlite3






"""          DATABASE'E VERİ EKLEMEK (INSERT)               """

# BU SEFER FONKSIYON HALİNE GETİRELİM.

def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers (FirstName,lastname,city,email)
                       values ('mert','ertürk','istanbul',
                               'mertterturkk@gmail.com') """)
                       
    connection.commit()
    connection.close()
    



    
"""         DATABASE'DE VERİ GÜNCELLEMEK          """



def updateCustomer():
    connection1 = sqlite3.connect("chinook.db")
    connection1.execute("""update customers set city = 'İstanbul', firstname = 'Mert',
                       lastname =' Ertürk' where city = 'istanbul' """)
                       
                       
    connection1.commit()
    connection1.close()
    
    
    
    
    
"""         DATABASE'DEN VERİ SİLMEK         """

# BU SEFER DE FONKSİYONA GİRDİ EKLEYELİM.

def deleteCustomer(customerid):
    connection2 = sqlite3.connect("chinook.db")
    connection2.execute(""" delete from customers where 
                        customerid = %d """ %(customerid))
    connection2.commit()
    connection2.close()