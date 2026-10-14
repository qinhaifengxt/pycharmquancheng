money = 10000
for i in range(1,21):

    import random
    score =random.randint(1,10)
    if score < 5:
        print(f"员工{i}，评分为{score}，低于5，不发工资，下一位")
        continue
    else:
        if money >= 1000:
           money = money - 1000
           print(f"员工{i}，评分为{score},发放工资一千，账户余额为{money}")
        else:
             print(f"员工{i}，评分为{score},工资已发完，下个月再来")
             break

