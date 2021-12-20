# -*- coding: utf-8 -*-
"""   Tue Jun 23 20:48:44 2020   @author: ERTURK
"""


def build_profile(first,last,**user_info):
    profile ={}
    profile["first_name"]=first
    profile["last_name"]=last
    for key, value in user_info.items():
        profile[key]=value
    return profile

user_profile=build_profile("albert","einstein",
                          location="princeton",
                          field="physics")
print(user_profile)


"""
BU FONKSIYON KULLANICIDAN KİŞİ HAKKINDA İSİM, SOYİSİM
VE KULLANICININ İSTEDİĞİ KİŞİ BİLGİLERİNİ EKLEMESİNİ SAĞLIYOR.
KİŞİ HAKKINDA VERİLECEK BİLGİLER KESİN DEĞİL.
YANİ BAŞKA BİRİSİNİ BU LİSTEYE EKLEDİĞİMİZDE ONUN YAŞI,
TELEFON NUMARASI GİBİ BİLGİLERİ DE EKLEYEBİLİRİZ. 
"""