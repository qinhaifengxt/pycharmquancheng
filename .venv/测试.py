# 拉格朗日插值法
# 用户输入数据，自行实现算法


# =========================
# 输入已知数据点
# =========================

n = int(input("请输入已知数据点个数："))

x = []
y = []

print("请依次输入每个数据点(x,y)：")

for i in range(n):

    xi = float(input(f"x[{i}]="))
    yi = float(input(f"y[{i}]="))

    x.append(xi)
    y.append(yi)


# =========================
# 输入要求值
# =========================

xx = float(input("\n请输入要求值x："))



# =========================
# 拉格朗日插值计算
# =========================

result = 0.0


for i in range(n):

    # 计算基函数Li(x)

    Li = 1.0

    for j in range(n):

        if i != j:

            Li = Li * (
                (xx - x[j])
                /
                (x[i] - x[j])
            )


    # 累加 yi*Li(x)

    result = result + y[i] * Li



# =========================
# 输出结果
# =========================

print("\n拉格朗日插值结果：")

print("P({}) = {:.6f}".format(xx, result))