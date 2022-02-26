import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("yatış günü.xlsx")


df["başvuru"]= df["başvuru (yıl)"].astype(str)+"-"+ df["başvuru (ay)"].astype(str)+"-"+ df["BAŞVURU  GÜN"].astype(str)
df['başvuru']= pd.to_datetime(df['başvuru'])

df.info()
#%%
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df["yatışın kaçıncı günü"] = df["üreme tarihi"]- df["başvuru"]

df["yatışın kaçıncı günü"] = df["yatışın kaçıncı günü"].dt.days.astype(int)

#%%

plt.figure()
plt.xlim(-50,250)
ax = df["yatışın kaçıncı günü"].plot.hist(bins=8,figsize=(10,5),rwidth=0.92)
ax.set_ylabel("")
ax2 = ax.twinx()
ax2= df["yatışın kaçıncı günü"].plot.kde()
ax2.set_ylabel("")
#ax.set_title("")
ax.set_xlabel("Gün")
ax.grid()
ax.set_xticks(list(range(0,250,40)))

plt.savefig('yatış_üreme.png', dpi=300)


