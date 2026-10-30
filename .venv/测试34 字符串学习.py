字符串1 = "itheima itcast boxuegu"
count = 字符串1.count("it")
print(f"字符串1 itheima itcast boxuegu中有：{count}个it字符")
字符串2=字符串1.replace(" ","|")
print(f"字符串1 itheima itcast boxuegu,被替换空格后，结果为：{字符串2}")
字符串3=字符串2.split("|")
print(f"字符串1 itheima itcast boxuegu按照|分隔后，得到：{字符串3}")