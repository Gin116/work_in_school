import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 定义文件路径
file_path = 'acc.txt'

# 读取数据
data = pd.read_csv(file_path, delim_whitespace=True)

# 选择需要的列
datasets = ["Cora", "Co.CS", "Am.Photos"]

# 定义不同的颜色和形状
colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink']
markers = ['o', 's', 'D', '^', 'v', '<', '>']

# 绘制每个数据集的图
for dataset in datasets:
    plt.figure(figsize=(10, 6))

    x_values = np.linspace(0, 1, len(data))  # 生成0到1之间的均匀分布的值
    y_values = [row[dataset] for index, row in data.iterrows()]  # 提取y轴上的值

    # 绘制一条折线
    plt.plot(x_values, y_values, color='black')

    # 绘制每种方法的数据点
    for index, row in data.iterrows():
        color = colors[index % len(colors)]
        marker = markers[index % len(markers)]
        plt.scatter(x_values[index], row[dataset], color=color, marker=marker, s=100, label=row["Methods"])

    # 添加图例，只显示一次
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # 设置图表标题和标签
    plt.title(f'Performance on {dataset}')
    plt.xlabel('Normalized Position')
    plt.ylabel('Accuracy')

    # 显示图表
    # plt.show()
    # 保存图表
    plt.savefig(f'{dataset}_performance.png')
    # 关闭图表以防止在循环中重叠
    plt.close()



