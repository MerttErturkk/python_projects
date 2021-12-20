# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:19:35 2021

@author: mertt
"""

import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_excel('sbie.xlsx')


etkenler = df["ETKEN"].value_counts()


etkenler.plot.bar()

#%%

klebsi = df[df["ETKEN"]=="KLEBSİELLA PNEUMONİAE"]

kleb_alan = klebsi["ALAN"].value_counts()

kleb_alan.plot.pie()



