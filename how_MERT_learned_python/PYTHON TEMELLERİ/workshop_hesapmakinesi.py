# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:35:47 2020

@author: ERTURK
"""
def hesapmakinesi():
    print("hesap makinesine hoş geldiniz \n ne işlem yapmak istersiniz?")
    a=str(input("\nçıkarma için '-'\ntoplama için '+'\nçarpma için'*\nbölme için '/' giriniz\n::"))
    sayı1=int(input("sayı 1 lütfen.\n"))
    sayı2=int(input("sayı 2 lütfen\n"))
    if a=="-":
        print(sayı1-sayı2)
    elif a=="+":
        print(sayı1+sayı2)
    elif a=="*":
        print(sayı1*sayı2)
    elif a=="/":
        print("sonuç "+str(sayı1/sayı2))
        