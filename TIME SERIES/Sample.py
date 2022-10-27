import pandas as pd
df=pd.read_csv('C:/Users/Yaw Asante/Dropbox/PYTHON/TIME SERIES/concise.csv')

print(df)


df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70