"""range(5,7,2)
for i in range(5,7,2):
    print(i)
"""
#range(10)：依次生成数字0到10，range（5,7）；生成数字5,6，选定指定起点和终点；range（0,10,3）：从零开始，每三个单位生成一个数字
count = 0
for i in range(1,100):
    if i % 2 == 0:
        count += 1
print(f"1到100有{count}个整数")
