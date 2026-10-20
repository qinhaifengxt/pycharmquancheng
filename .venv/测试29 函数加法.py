"""
def add(x,y):
    return x + y
q = add(3,4)
print(q)

def add(x,y):
    x=int(input())
    y=input()
    q = x + y
    print(f"{q}")


add(1,4)
"""
def add(x,y):
    q = x+y
    print(f"{q}")

a = add(3,4)
print(f"a的数据类型是：{type(a)},a的内容是{a}")
if a:
    print("我是菜逼")
if not a:
    print("我很牛逼")