import pandas as pd
import shutil

#%% read the csv and reset the index

df= pd.read_csv(("bee_data.csv"))

russ = df[df["subspecies"]=="Russian honey bee"].reset_index()
carni = df[df["subspecies"]=="Carniolan honey bee"].reset_index()

#%% filter the dataframes to only include columns related to our task
filtered_russ = russ[["file","subspecies","health"]]

filtered_carni = carni[["file","subspecies","health"]]

#%%  combine two dataframe together
new_df = pd.concat([filtered_carni,filtered_russ],join="outer").reset_index()

new_df= new_df[["file","subspecies","health"]]

#%% save the csv

new_df.to_csv("ml_bees.csv",index=False)

#%% move the russian honey bees to different directory
for file in new_df["file"]:
    direc= "bee_imgs/" + file
    shutil.move(direc, "bee_imgs/russ&carni")
    
