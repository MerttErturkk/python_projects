# -*- coding: utf-8 -*-
"""   Mon Jun 29 00:06:23 2020   @author: ERTURK
"""

import sqlite3

connection = sqlite3.connect("chinook.db") 


"""         LIKE    """
# İÇİNDE "A" HARFİ GEÇEN İSİMLİ MÜŞTERİLER GİBİ.

cursor = connection.execute("""select FirstName,LastName from customers
                            where FirstName like '%a%' """)
                            
for row in cursor:
    print(row[0] + " " + row[1])
    
    
print("\n\n\n\n\n\n\n")



# İSMİ "A HARFİ İLE BAŞLAYAN MÜŞTERİLER GİBİ.

cursor1 = connection.execute("""select FirstName,LastName from customers
                            where FirstName like 'a%' """)
                            

for row in cursor1:
    print(row[0] + " " + row[1])

# Eğer "like '%a' " olarak bitirseydim FirstName'i "a" ile bitenler gelirdi.
# % işareti arkasında yada önünde ne olduğunun önemi yok demek.