import random

# 生成随机数
number = random.randint(1, 100)

# 设置初始次数和状态标志
count = 0
is_win = False

# 提示用户进行猜测
print("我想了一个数字，请你猜一猜。")
while count < 10:
    guess = int(input("请猜一个 1-100 的整数："))
    count += 1
    if guess == number:
        print("恭喜你，你猜对了！你总共猜了 %d 次。" % count)
        is_win = True
        break
    elif guess > number:
        print("太大了，请再试一次。")
    else:
        print("太小了，请再试一次。")

if not is_win:
    print("很遗憾，你没有在规定次数内猜对，正确答案是 %d。" % number)