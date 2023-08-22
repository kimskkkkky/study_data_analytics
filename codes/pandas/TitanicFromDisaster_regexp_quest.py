import pandas as pd

df_TFD = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
data = df_TFD['Name']
df_TFD_name = pd.DataFrame(data)
print(df_TFD_name)

pattern = r'^([A-Za-z]+)'
df_TFD_extract = df_TFD_name['Name'].str.extract(pattern)
print(df_TFD_extract)



