答案 = 10
"""if int(input("第一次输入的数字")) == 10:
    print("第一次就猜对了")
elif int(input("第二次输入的数字")) == 10:
    print("第二次就猜对了")
elif int(input("第三次输入的数字")) == 10:
    print("第三次猜对了")
else:
    print("三次全错，答案是10")"""

if int(input("第一次输入的数字")) != 10:
    print("第一次就猜错了")
elif int(input("第二次输入的数字")) != 10:
    print("第二次就猜对了")
else:
    print("第三次猜了")
