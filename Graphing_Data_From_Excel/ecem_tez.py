# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:19:35 2021

@author: mertt
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = '5'
#%%
df = pd.read_excel('sbie.xlsx')
etkenler = df["ETKEN"].value_counts()
etkenler.plot.bar()
#%%
klebsi = df[df["ETKEN"]=="KLEBSİELLA PNEUMONİAE"]
kleb_alan = klebsi["ALAN"].value_counts()
#%%
kleb_alan.plot.pie()

#%%#######################################################

df = pd.read_excel("MELFLİ GÜNCEL SONN.xls")
df = df[0:105]
evre_melf = df[["Evre2","MELF"]]
#%%
evre1 =evre_melf[evre_melf["Evre2"]==1]
evre1_val =evre1.value_counts().to_list()
#%%
evre2 =evre_melf[evre_melf["Evre2"]==2]
evre2_val =evre2.value_counts().to_list()
#%%
evre3 =evre_melf[evre_melf["Evre2"]==3]
evre3_val =evre3.value_counts().to_list()
#%%
e_melf_x=["EVRE1_MELF(+)","   EVRE1_MELF(-)","",
          "EVRE2_MELF(+)","   EVRE2_MELF(-)"," ",
          "EVRE3_MELF(+)","   EVRE3_MELF(-)"]
e_melf_y = evre1_val +[0]+ evre2_val +[0]+ evre3_val
#%%

COLOR =["red","blue","black","red","blue","red","red","blue"]
plt.bar(x=e_melf_x, height =e_melf_y, color=COLOR)
plt.show()
plt.savefig('evre_melf.png', dpi=1000)
















