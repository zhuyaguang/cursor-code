# 打开文件
with open('robot.txt', 'r') as file:
    # 初始化计数器
    count = 0
    # 遍历每一行
    for line in file:
        # 如果找到了 “######” 在该行，增加计数器值
        if '######' in line:
            count += 1
    # 输出结果
    print("包含有 ###### 的行数: ", count)
    