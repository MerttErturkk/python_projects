import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("yaşlar.xlsx")

# inspect column names
cols = df.columns
cols = list(cols)
#%%

new_cols= ["hastane/toplum","tarih","dt"]
col_dict=dict(zip(cols,new_cols))

#assign easier to manage names
df= df.rename(columns=col_dict)


df["dt"] = pd.to_datetime(df["dt"])

#calculate age
df["yaş"]=df.tarih - df.dt


#%% inspect the distribution
cnt = df["hastane/toplum"].value_counts()
print(cnt)

#%%

df["yaş_ay"]=(df.yaş / np.timedelta64(1, 'D')/30).astype(int)

x=df[df["hastane/toplum"]==1]


#%%
plt.figure()
plt.xlim(-50,240)
ax = x.yaş_ay.plot.hist(bins=18,figsize=(10,5),rwidth=0.92)
ax.set_ylabel("")
ax2 = ax.twinx()
ax2= x.yaş_ay.plot.kde()
ax2.set_ylabel("")
ax.set_title("Hastane Enfeksiyonu")
ax.set_xlabel("Yaş(Ay)")
ax.grid()
ax.set_xticks(list(range(0,240,24)))
plt.savefig('HASTANE.png', dpi=300)



