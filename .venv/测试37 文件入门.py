#f = open(r"C:\python文件测试\新建 文本文档.txt",'r',encoding='utf-8')
#content = f.read(15)

#print(content)

# """
# f = open(r"C:\python文件测试\新建 文本文档.txt",'r',encoding='utf-8')
# content = f.readline()
# content2 = f.readline()
# print(content)
# print(content2)
# """
f = open(r'C:\python文件测试\新建 文本文档 (2).txt','r',encoding='utf-8')
count = 0
for line in f:
    line1 =line.strip()
    words=line1.split(' ')
    for word in words:
        if word =='a':
            count += 1
print(count)


f = open(r"C:\python文件测试\新建 文本文档 (2).txt",'r',encoding='utf-8')
content = f.read()
print(content.count('a'))
f =open(r"C:\python文件测试\新建 文本文档 (2).txt",'w',encoding='utf-8')
f.write('国服第一剑圣秦海峰')
f.flush()
f.close()


