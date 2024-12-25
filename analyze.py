import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


game_data = pd.read_csv('/Users/zhangboxiang/Desktop/project for data/project-for-data-analyze/vgsales.csv')


print(game_data)

# 对数据中的非数值列进行编码，例如 'Platform', 'Publisher' 等
# 先检查数据中的非数值列
print(game_data.dtypes)

# 使用 LabelEncoder 将分类数据转换为数值类型
label_encoder = LabelEncoder()

# 假设 'Platform' 和 'Publisher' 是类别数据
game_data['Platform'] = label_encoder.fit_transform(game_data['Platform'])
game_data['Publisher'] = label_encoder.fit_transform(game_data['Publisher'])

# 将 'Genre' 列作为目标变量，其他列作为特征
x = game_data.drop(columns=['Genre'])
y = game_data['Genre']

# 输出特征和目标变量
print(x)
print(y)

# 创建模型并训练
model = DecisionTreeClassifier()
model.fit(x, y)
