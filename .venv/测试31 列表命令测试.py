list = [21,25,21,23,22,20]
# list末尾增加元素格式
# list.append()
# list查找元素位置格式
# list.index()
# list修改元素格式
# list[]=变换后的值
# list插入元素格式
# list.insert(选择的位置——不需要中括号，要加的元素）
# list后面也能追加列表
"""
list = [1,2,3,4,5,6,7,8,9,10]
list1 = [2,3,4]
list.extend(list1)
"""
# list删除某个元素
# del 列表[]
# list.pop[]
# 清除列表
# list.clear()
# 统计list列表中某个元素的格式
# list.count(要查找的元素)
# 统计list 列表元素的个数
# len(list)
list.append(31)
print(list)
list2 = [29,33,30]
list.extend(list2)
print(list)
q=list.pop(0)
print(f"list取出的元素是:{q}，list列表现在为：{list}")
list.pop(-1)
print(list)
q=list.index(31)
print(f"元素31在列表的位置是：{q}")

