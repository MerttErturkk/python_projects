# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("chinook.db") 

"""                         BY                             """

# En çok müşterinin olduğundan en az müşterinin olduğu şehre doğru sırala.
# ilk müşteri sayısına göre sonra alfabetik olarak sıraladım.
cursor = connection.execute("""select city,count(*) from customers
                            group by city order by count(*) desc,city""")
                            # "order by *** " hep sona yazılır.
    
for row in cursor:
    print("City = " + row[0])
    print("Count =" + str(row[1]))
    
 



"""                        HAVING                     """
print("\n\n\n\n\n\n\n")


# Birden fazla müşterinin olduğu şehirleri isme göre sırala.
cursor1 = connection.execute("""select city,count(*) from customers
                            group by city having count(*)>1 
                            order by city""")
                            
    
for row in cursor:
    print("City = " + row[0])
    print("Count =" + str(row[1]))



connection.close()