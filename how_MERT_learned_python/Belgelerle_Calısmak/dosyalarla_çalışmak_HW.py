# -*- coding: utf-8 -*-
"""   Fri Jun 19 15:43:57 2020   @author: ERTURK
"""

öğrenciler=["engin","derin","salih","ali","ayşe"]

filetoappend= open("öğrenciler.txt","a") # eğer yoksa aynı zamanda
for öğrenci in öğrenciler:               # dosyayı oluşturur.
    filetoappend.write(öğrenci)
    filetoappend.write("\n")

filetoappend.close()
