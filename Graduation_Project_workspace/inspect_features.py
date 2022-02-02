import pandas as pd
df = pd.read_csv("features_30_sec.csv")


print(str(df.head()) + "\n***************************************************************")
print(str(df.info()) + "\n***************************************************************")
pd.set_option('display.max_columns', 60)
print(df.describe())    