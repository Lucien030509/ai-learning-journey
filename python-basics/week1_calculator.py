# ===== 这就是你写的第一个程序：计算器 =====
# 先运行一遍看看效果，然后我会逐行解释

print("===== 我的计算器 =====")
print("输入两个数字，我帮你算")

# 让用户输入两个数字
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))

# 加减乘除
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

# 除法要特别处理：不能除以 0
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("不能除以 0 ！")
