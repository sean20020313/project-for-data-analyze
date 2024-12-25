import pandas as pd
df = pd.read_csv('/Users/zhangboxiang/Desktop/project for data/project-for-data-analyze/vgsales.csv')
print(df.shape)
print(df.describe)
print(df.values)