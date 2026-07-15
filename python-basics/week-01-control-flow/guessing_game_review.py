
known = 7
guess = 0
attempts = 0

print("我想好了一个1到10的数字")

while guess != known and attempts < 3:
    guess = int(input("请输入你猜的数字："))
    attempts = attempts + 1
    if guess == known:
        print(f"猜对了,你猜了{attempts}次")
    elif guess < known:
        print("猜小了")
    else:
        print("猜大了")
if guess != known:
    print(f"3次机会用完了，正确答案是{known}")
        
