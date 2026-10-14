import random
num = random.randint(1,10)
guess_num = int(input("请第一次输入数字："))
if num == guess_num:
    print("恭喜第一次就猜对")
else:
    if num > guess_num:
        print("猜小了")
    else:
        print("猜大了")
    guess_num = int(input("请第二次次输入数字："))
    if num == guess_num:
        print("恭喜第二次就猜对")
    else:
        if num > guess_num:
            print("猜小了")
        else:
            print("猜大了")
        guess_num = int(input("请第三次输入数字："))
        if num == guess_num:
            print("恭喜第三次猜对")
        else:
            print("三次都不对")

