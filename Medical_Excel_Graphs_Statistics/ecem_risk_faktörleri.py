import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = '5'

#%%
a="""Santral Katater
Antiepileptik Kullanımı
İntravenöz Sıvı Kullanımı
Nazogastrik Tüp
PPİ/H2 Blokör Kullanımı
Ventilasyon: Entübe/Trakeostomi
Sedasyon
Transfüzyon
Sistemik Kortikosteroid Kullanımı
Postoperatif Dönem
İdrar Sonda Varlığı
Total Parenteral Nütrisyon
Kardiyopulmoner Resusitasyon
İnotrop İhtiyacı
Perkütan Endoskopik Gastrostomi
Periferik Katater
Diyaliz
İmmünsupresyon
Plazmaferez
Eksternal Ventriküler Drenaj
Dekübit Yarası
Kolostomi
Toraks Tüpü
Biyopsi
"""
items =a.splitlines()
percentages= [66.7,62.2,61.3,58.6,57.7,49.5,46.8,
              31.5,27.9,25.2,23.4,20.7,17.1,13.5,
              13.5,11.7,9,7.2,5.4,5.4,3.6,2.7,1.8,0.9]
#%%


y_pos = np.arange(len(items))
plt.figure()#figsize=(10,10))
plt.barh(y_pos, percentages,align='center')
plt.yticks(y_pos,items,fontsize=7)
plt.xlabel('%')
plt.gca().invert_yaxis()
plt.xlim(0,70)
plt.title('Risk Faktörleri')
plt.grid()
plt.tight_layout()
plt.savefig('ecem.png', dpi=300)