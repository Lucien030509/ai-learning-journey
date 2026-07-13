# ===== 猜数字游戏 =====
import random  # 导入随机数模块

# 电脑随机想一个 1-100 的数
secret = random.randint(1, 50)
print("我想到一个 1 到 50之间的数字，你猜是多少？")

guess = 0       # 先给 guess 一个初始值
attempts = 0    # 记录猜了几次

# while 循环：只要没猜对就一直猜
while guess != secret:
    guess = int(input("输入你猜的数字: "))  # int() 把输入变成整数
    attempts = attempts + 1

    if guess > secret:
        print("大了，再猜小一点")
    elif guess < secret:
        print("小了，再猜大一点")
    else:
        print(f"猜对了！数字就是 {secret}，你一共猜了 {attempts} 次")
