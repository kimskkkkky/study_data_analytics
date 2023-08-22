import pandas as pd

df_TFD = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
data = df_TFD['Name']
df_TFD_name = pd.DataFrame(data)
print(df_TFD_name)

# 성 뽑아낸 후 컬럼 생성

pattern = r'^([A-Za-z]+)'
df_TFD_name['firstname'] = df_TFD_name['Name'].str.extract(pattern)
print(df_TFD_name)

# 결혼한 사람만 뽑아낸 후 컬럼 생성

pattern = r'(Mrs?)'
df_TFD_name['marry'] = df_TFD_name['Name'].str.extract(pattern)
df_TFD_name=df_TFD_name.dropna()
print(df_TFD_name)


