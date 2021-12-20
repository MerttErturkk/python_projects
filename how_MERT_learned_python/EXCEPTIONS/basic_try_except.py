

try:
    sayi = int(input("sayı giriniz: "))
    print("devam")
except:
    print("Hata oluştu.")



print("""\n\n
try except sayesinde error olsa da 
olmasa da kodun geri kalanı çalıştı.""")

"""
Bu kodu ayrıca,

try:
    sayi = int(input("sayı giriniz: "))
    print("devam")
except ValueError:
    print("Tip Uyuşmazlığı hatası oluştu.")
except:
    print("Hata oluştu")
    
    
şeklinde de yazabilirdik.
"""
    



