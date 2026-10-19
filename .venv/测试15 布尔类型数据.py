# 联系布尔数据类型，顺道复习前面的字符串格式化 !=是不等于的意思，==是等于的意思
变量1 = True
变量2 = False
print("变量1的数据类型为：%s"%type(变量1))
print(f"变量2的数据类型为：{type(变量2)}")
# 联系下比较运算符
bool1 = 10>5
print(f"bool1的输出结果为：{(bool1)},数据类型为：{type(bool1)}")
bool1 =10
bool2 =15
print(f"bool大于bool2的结果为：{bool1>bool2},{type(bool1>bool2)}")
