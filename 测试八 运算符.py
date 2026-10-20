""""
数字运算符：+、/、*、-、**(指数）、%（取余）、//（整除）
a+=a  等价于 a=a+a
a/=a  等价于 a=a/a




"""
a = 3
print("a+a:",a+a)
print("a/a:",a/a)
a = 6
a+=2
print("a+2:",a)
a/=2
a=16
print("a/2:",a)
a**=2
print("a**2:",a)
a//=5 #a=a/5（结果取整）
print("a//5:",a)
a = 13
a%=3
print("a%3:",a)
