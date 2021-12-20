# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""

CLASSLAR  ===   NESNELERİN ORTAK NOKTALARINDA TOPLAMAK.
                  İLGİLİ NESNELERI SINIFLANDIRMAK.
                  
                  
                aşağıdaki koda "self" parametresini sunmam gerekli.
                
                (NEDENINI PEK ANLAMADIM, NESNEl PROGRAMLAMA ÖĞRENMEM GEREKİYOR.)
                
                "self" önceden bellekte oluşturduğumuz "Matematik"classına
                yani kendisine refer ediyor, ve ben "sayı1"i ilk
                parametre olarak verdiğimde onu "self" olarak anlıyor ve
                iki parametre yerine 3 parametre verdin errorü veriyor.
                
                eğer ben sisteme sadece bir parametre verirsem o 
                parametre "sayı2" olarak kabul edilecek ve " "Matematik" nesnesi
                ile integer olan "sayı2"yi toplayamadım" " erroru alınacak.
                
                
"""
class Matematik:
    def topla(self,sayı1,sayı2):
        return sayı1+sayı2
    def çıkar(self,sayı1,sayı2):
        return (sayı1-sayı2)
    def çarp (self,sayı1,sayı2):
        return sayı1*sayı2
    def böl(self,sayı1,sayı2):
        return (sayı1/sayı2)
    
    
matematik=Matematik()
