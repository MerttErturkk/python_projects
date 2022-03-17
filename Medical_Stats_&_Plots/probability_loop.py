#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%

df = pd.read_excel(r"antibiyotikler-dirençler-yıllar-etkenler.xlsx")
# inspect column names
cols = df.columns
cols = list(cols)
#%%


"""
klebsiella spp      19
pseudomonas spp     18
"""

x=df["başvuru (yıl)"].value_counts()
#print(x)

y2017 = df[df["başvuru (yıl)"]==2017]
y2018 = df[df["başvuru (yıl)"]==2018]
y2019 = df[df["başvuru (yıl)"]==2019]
y2020 = df[df["başvuru (yıl)"]==2020]
y2021 = df[df["başvuru (yıl)"]==2021]


#print(y2017.iloc[:,3:-2].describe())
#%%

x = y2020[y2020["etken"]=="klebsiella spp"]
antibiyotikler=x.iloc[:,3:-2]
series=[]
print("ETKEN == klebsiella spp\n2020\nvaka sayısı(n)  = "+str(len(x)))
for i in antibiyotikler:
    print("\n"+i)
    y=antibiyotikler[i]
    print(list(y[y==2].value_counts()))
    print(list((y[y==2].value_counts()/len(x)).round(3)))
    

#%%

    