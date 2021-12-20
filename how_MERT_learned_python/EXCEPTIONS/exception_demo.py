# -*- coding: utf-8 -*-
import sys
liste = ["mert",0,3,"a",["aaa","aa"]]
i=1
for x in liste:
    
    try:
        print("satı: "+ str(x))
        sonuc = 1/int(x)
        print("sonuc : "+str(sonuc))
    except ValueError:
        print(str(i)+". eleman "+str(x)+ " bir sayı değil.")
    except ZeroDivisionError:
        print(str(i)+". eleman "+str(x)+ " sıfıra bölünmez")
    except:
        print("HATA : "+ str(sys.exc_info()[0]))
    finally:
        print("işlemler bitti.")
    i=i+1  
        
## sys programın verdiği hataları görmemizi sağlar.

## finally try except fark etmezsizin işlem sonunda çalışır.
