import pandas as pd
import matplotlib.pyplot as plt

# 定义文件路径
file_path = 'acc.txt'

# 读取数据
data = pd.read_csv(file_path, delim_whitespace=True)

# 选择需要的列
columns_to_plot = ["Methods", "Cora", "Co.CS", "Am.Photos"]
data_selected = data[columns_to_plot]

# 设置图的大小
plt.figure(figsize=(10, 6))
# 绘制每种方法的数据
for index, row in data_selected.iterrows():
    if row["Methods"] == "BDM":
        plt.plot(["Cora", "Co.CS", "Am.Photos"], row[1:], label=row["Methods"], linewidth=3)  # 设置BDM方法的线条加粗
    else:
        plt.plot(["Cora", "Co.CS", "Am.Photos"], row[1:], label=row["Methods"])

# 添加图例
plt.legend()

# 设置图表标题和标签
plt.title('Performance of Different Methods')
plt.xlabel('Dataset')
plt.ylabel('Value')

# 显示图表
# plt.show()
plt.savefig("./Performance of Different Methods.png")