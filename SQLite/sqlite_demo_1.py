import sqlite3

connection = sqlite3.connect("chinook.db") 
                        # eğer böyle bir dosya yoksa onu oluşturur.


cursor = connection.execute("select * from customers")
                            # ("select FirstName, LastName from customers")
                            # üstteki gibi isteseydik bizim ilk sütun verimiz
                            # yani "0". column FirstName column'ı olacaktı
                            # "*" bütün elemanları getirir. bu yüzden 
                            # 0. column dosyada olduğu gibi CustomerId.

for row in cursor:
    print("First name: "+ row[1])
    
# daha detaylı bi örnek 
cursor1= connection.execute("""select FirstName,LastName from customers 
                            where City = 'Prague' or city ='Berlin'
                            order by LastName desc""") # order by LastName asc
                                                  # olsaydı tersten sıralardı.
                                                  # "asc" = ascending
                                                  # küçükten büyüğe doğru
                                                  # 1,2,3 yada a,b,c
                                                  # "desc" = descending
                                                  # büyükten küçüğe doğru
                                                  # 3,2,1 ada c,b,a
                                                  # default'u "asc"dir.
                                                  
                          
print("""\n\nCUSTOMERS FROM PRAGUE OR BERLIN
      \n-----------------------""")
      
for row in cursor1:
    print(row[0]+" "+row[1])
    print("***")

connection.close()    