def read_data(file_path, grid_width):
    coordinates = []

    with open(file_path, 'r') as file:
        for line in file:
            # 将每行数据按空格分割
            parts = line.strip().split()
            if len(parts) == 2:
                node, community = parts
                node = float(node)
                community = int(community)

                # 计算二维坐标
                x = node // grid_width
                y = node % grid_width

                # 添加坐标和社区编号
                coordinates.append(((x, y), community))

    return coordinates


# 示例使用
file_path = 'Cora-labels.txt'
grid_width = 52  # 选择适当的宽度，使得2708个节点可以被均匀分布在网格中
coordinates = read_data(file_path, grid_width)

# 打印前10个坐标作为示例
for coordinate in coordinates[:10]:
    print(coordinate)
