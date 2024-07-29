import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path = 'rec.xlsx'
data = pd.read_excel(file_path)

# 定义颜色和形状
colors = ['red', 'blue', 'green']
markers = ['o', 's', 'D']

# 获取所有的独特数据集
datasets = data['Datasets'].unique()

# 绘制每个数据集的图
for dataset in datasets:
    plt.figure(figsize=(10, 6))

    # 筛选出当前数据集的数据
    subset = data[data['Datasets'] == dataset]

    # X轴的刻度（百分比）转换为0.1到1之间的值
    x_labels = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%']
    x_values = np.linspace(0.1, 1, len(x_labels))  # 生成0.1到1之间的均匀分布的值

    # 为每种方法绘制折线
    for i, method in enumerate(subset['Methods'].unique()):
        method_data = subset[subset['Methods'] == method]
        y_values = method_data.iloc[0, 2:]  # 提取从第3列开始的数据

        plt.plot(x_values, y_values, color=colors[i], marker=markers[i], linestyle='-', label=method)

    # 设置x轴的刻度标签
    plt.xticks(x_values, x_labels)

    # 设置图表标题和标签
    plt.title(f'Performance on {dataset}')
    plt.xlabel('Fraction of Data')
    plt.ylabel('Accuracy')

    # 添加图例
    plt.legend(title='Methods')

    # 保存图表
    plt.savefig(f'{dataset}_recall_performance.png')

    # 关闭图表以防止在循环中重叠
    plt.close()
