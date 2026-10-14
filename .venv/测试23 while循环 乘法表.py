
# /t 制表符，第一行对齐 end='' 不换行输出  print() 等于换行
"""i=1
while i<=9:
    j=1
    while j<=i:

        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print()
"""
"""
i=1

while i<=9:
    j=i
    while j>=i and j<=9:

        print(f"{i}*{j}={j*i}")
        j+=1
    i+=1
    print()
"""
i = 0
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={i*j}\t",end='')
        j+=1
    i +=1
    print()