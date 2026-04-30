import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Катя", "Иван", "Тима", "Катя", "Олег"],
    "age": [25, 17, None, 25, 200],
    "city": ["BISHKEK", "bishkek", "bishkek", "BISHKEK", "Moskva"],
    "salary":[10000,22000,None,10000,80000]
})

print(df.head())
print(df.info())
print(df.describe())
print("======================")

# df = df.drop_duplicates()
print(df.head())
print("==============================")
# df = df[df['age'] < 100]
# df['age'] = df['age'].fillna(df['age'].mean())
df['salary']=df['salary'].fillna(df['salary'].mean())

df['city']=df['city'].str.lower()
df['city']=df['city'].replace({'moskva':'moscow'})


print(df.head())
print(df.isnull().sum())

df_drop_age=df.dropna(subset=['age'])
print(df_drop_age)

df_fill=df.copy()
df_fill['age_mean']=df_fill['age'].fillna(df_fill['age']).mean()

df_fill['age_median']=df_fill['age'].fillna(df_fill['age']).median()

print(df_fill)
df_fill=df_fill.drop('age_mean',axis=1)

df_fill['age']=df_fill['age'].fillna(df_fill['age'].median())
df_fill['city']=df_fill['city'].str.title()
print(df_fill)



# ================Группировка=======
result = df_fill.groupby('city').agg({
    'salary': 'mean',
    'age': 'median'
})

print(result)
df_fill['is_adult'] = df_fill['age'] >= 18
print(df_fill)




