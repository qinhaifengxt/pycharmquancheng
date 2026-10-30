

f =open(r"C:\Users\28161\Desktop\pycharm测试项目文件夹\练习.txt",'r',encoding='utf-8')
f1 = open(r"C:\Users\28161\Desktop\pycharm测试项目文件夹\bill.txt",'a',encoding='utf-8')
for line in f:
    words =line.strip()
    new_words = words.split(',')

    if new_words[4] == '测试':
        continue
    else:
        f1.write(words)
        f1.write('\n')
        f1.flush()


