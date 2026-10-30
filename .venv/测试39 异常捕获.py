try:

    print(变量1)
except NameError as e:
    print('程序出错了')

try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')
try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    print(e)
try:
    f = open('test.txt', 'r')
except Exception as e:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()
