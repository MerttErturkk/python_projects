# Starting off with the Server Connection
import pyodbc
# for driver in pyodbc.drivers():
#     print(driver)

DRIVER= "SQL Server"
SERVER= ".\mssqlserver02"
DATABASE = "testdb_mert"


conn = pyodbc.connect(f'Driver={DRIVER};'
                      f'Server={SERVER};'
                      f'Database={DATABASE};'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#%%
cursor.execute("""CREATE TABLE Table_1
                    (employee varchar(50),
                    Age int);
                    """)
conn.commit()
#%%
entries = [["mert",23],["jonathan",60]]

insert_query= """INSERT INTO  [dbo].[Table_1](employee,Age)
                 VALUES (?,?);"""
                 # "?" is the place holder in pyodbc 

for row in entries:
    cursor.execute(insert_query,row) # or selected items as tuple
conn.commit()

#%% Fetching the Result
cursor.execute("SELECT * FROM Table_1")

for row in cursor.fetchall():
    print(row)
#%% Adding Primary Identity Key
cursor.execute("""
               ALTER TABLE [dbo].[Table_1]
               ADD id INT PRIMARY KEY IDENTITY(1,1);
               """)
               
#%% Closing the connection
cursor.close()
conn.close()

#%%============================================================================
# TESTING WITH A PROPER DATABASE TABLE
#=========================================================================== 

query="""SELECT TOP (3) [AddressID]
      ,[AddressLine1]
      ,[AddressLine2]
      ,[City]
      ,[StateProvinceID]
      ,[PostalCode]
      ,[SpatialLocation]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[Person].[Address]
  """
cursor.execute(query)


# Save the result as tuple
result=tuple(cursor)
for entry in result:
    print(entry)
    
#%%===========================================================================
# TESTING PANDAS DATAFRAME
# =============================================================================
import pandas as pd
pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1)

query="""SELECT TOP (1000) [AddressID]
      ,[AddressLine1]
      ,[AddressLine2]
      ,[City]
      ,[StateProvinceID]
      ,[PostalCode]
      ,[SpatialLocation]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2019].[Person].[Address]
  """

df = pd.read_sql(query,conn)
#%% INSPECT THE TABLE
print(df.info())
print(df)

print("\n\n\n")
print(df["City"].head())
print("\n\n\n")
print(df["City"].value_counts())
filtered_df=df[(df["City"]=="Seattle" ) | (df["City"]=="Everett")]

subset_filtered_df = filtered_df[["PostalCode","AddressLine1"]]
print(subset_filtered_df.info())

#%%  SAVE THE RESULTING TABLE AS EXCEL
subset_filtered_df.to_excel("filtered_database.xlsx",
             sheet_name='Sheet_1')








