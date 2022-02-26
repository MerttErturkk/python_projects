#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


df = pd.read_excel("antibiyotikler-dirençler.xlsx")
# inspect column names
cols = df.columns
cols = list(cols)
hastane=df[df["HastaneEnfeksiyonu/Toplum kaynaklı"]==1]
toplum=df[df["HastaneEnfeksiyonu/Toplum kaynaklı"]==2]

#%%
# =============================================================================
# np.corrcoef()
# from scipy import stats
# corr,p=stats.pearsonr(a,b)
# =============================================================================
sub_has=hastane[["karbapenem direnci","metisilin direnci","kolistin direnci","vanko direnci","esbl"]]
sub_top=toplum[["karbapenem direnci","metisilin direnci","kolistin direnci","vanko direnci","esbl"]]
print(sub_has.describe())

print("\n\n")
for i in sub_has.columns:
    print(sub_has[i].value_counts())
    print("\n")
    
#%%

plt.figure(figsize=(10,5))
plt.xlim(-2,26)
val_cnt= hastane["kaç gundur antb alıyor"].value_counts()
plt.bar(val_cnt.index,height=val_cnt.values)
plt.tight_layout()
plt.grid()
plt.title("Antibiyotik Kullanımı")
plt.xlabel("Gün")
plt.xticks(list(range(0,26)))
plt.savefig('Antibiyotik Kullanımı.png',bbox_inches='tight', dpi=300)


#%%

antibiyotikler=toplum.iloc[:,12:]
series=[]
print("TOPLUM\n\n")
for i in antibiyotikler:
    print("\n"+i)
    y=antibiyotikler[i]
    print(list(y[y==2].value_counts()))
    print(list((y[y==2].value_counts()/len(toplum)).round(3)))