# 三种变量查询方式 第一种
print(type(666))
print(type(13.14))
print(type("国服第一剑圣"))
# 三种变量查询方式 第二种
变量1 = type(666)
变量2 = type(13.14)
变量3 = type("国服第一剑圣")
print(变量1)
print(变量2)
print(变量3)
# 三种变量查询方式 第三种
变量1 = 666
变量2 = type(变量1)
print(变量2)
