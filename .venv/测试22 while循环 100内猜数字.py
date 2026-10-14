import random
number=random.randint(1,100)
a = True
次数 = 0
while a:
    guess_number = int(input("请输入数字："))
    次数 +=1
    if guess_number == number:
        print("你猜对了")
        a = False
    else:
        if guess_number > number:
           print("你猜大了")
        else:
           print("你猜小了")
print("你猜测的次数：%d"%次数)
