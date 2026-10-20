#黑马atm
money = int(input("请输入您的余额"))
name =input("请输入名字")
def main():
    print(f"{name},欢迎来到黑马银行ATM，请选择操作：")
    print("余额查询：\t\t【请输入1】")
    print("存款：\t\t【请输入2】")
    print("取出：\t\t【请输入3】")
    print("退出：\t\t【请输入4】")
def yuer():
    global money
    print(f"您的余额为{money}")
def cunkuan(num):
    global money
    num= int(input("请输入数字"))
    money += num
    print(f"您本次存款{num}，您的余额为{money}")
def quqian(num):
    global money
    num= int(input("请输入数字"))
    money -= num
    print(f"您本次取钱{num}，您的余额为{money}")
def exit():
    print("您已退出程序")
while True:
    main()
    caozuo = int(input("请输入操作数字"))
    if caozuo == 1:
        yuer()
    elif caozuo == 2:
        cunkuan(1)
    elif caozuo == 3:
        quqian(1)
    else:
        exit()
        break