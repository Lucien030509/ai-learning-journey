import random
secret = random.randint(1,10)
guess = 0
attempts = 0
print("我想到一个 1 到 10 之间的数字，你猜是多少？")
while guess != secret and attempts < 5:
    print("现在开始新一轮测试")
    guess = int(input("请输入数字："))
    if guess <1 or guess > 10:
        print("请输入 1 到 10")
        continue
    attempts = attempts + 1
    if guess > secret:
        print("大了，再猜小一点")
    elif guess < secret:
        print("小了，再猜大一点") 
    else:
        print(f"猜对了！数字就是 {secret}，你一共猜了 {attempts} 次")
if guess != secret:
    print(f"5 次机会用完了，正确答案是 {secret} ")