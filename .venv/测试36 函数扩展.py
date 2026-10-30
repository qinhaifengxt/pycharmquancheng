


"""def 函数():
    return '剑圣','第一','国服','秦海峰'
x,y,z,q =函数()
print(x,y,z,1)

def fuhe(aa):
    result = aa(1,4,6)
    print(result)

def limian(x,y,z):
    result = x+y+z
    print(result)


a =fuhe(limian)
print(a,type(limian))

"""

def fuhe(func):
    result = func(1, 4, 10)
    print(result)

def limian(x, y, z):
    result = x+y+z
    print(result)



fuhe(limian)  # 输出 15
"""# lambda函数练习
def fehe(a):
    resulu = a(1,2,3)
    print(resulu)

fehe(lambda x,y,z:x+y)

"""