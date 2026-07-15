# ===== 九九乘法表 =====

# 外层循环：i 从 1 到 9
for i in range(1, 10):
    # 内层循环：j 从 1 到 i
    for j in range(1, i + 1):
        # end="" 表示打印完不换行
        print(f"{j}×{i}={i * j}", end="\t")
    # 一行打完，换行
    print()
