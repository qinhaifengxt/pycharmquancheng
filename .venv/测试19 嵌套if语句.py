"""age =int(input("输入你的年龄"))
level =int(input("输入你的等级"))
time =int(input("输入你的入职时间"))
if age >= 18:
    print("你是成年人。")
    if age<30 and time >2:
        print("你可以获得礼物")
    elif level>3:
       print("你可以获得礼物")
    else:
       print("你没有礼物")
else:
    print("你没有礼物")"""

#以下为自己想法
age =int(input("输入你的年龄"))
level =int(input("输入你的等级"))
time =int(input("输入你的入职时间"))
if age >= 18 and age <=30:
    if level>=3:
      print("you can get gift")
    elif time>2:
        print("you can get gift")
    else:
        print("you can not get gift")
else:
    print("you can not get gift")