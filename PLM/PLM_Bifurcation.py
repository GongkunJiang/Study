#-*-coding:utf-8-*-
import numpy as np
import matplotlib.pyplot as plt
def PLM(U,x):
    # N=64
    # M = float(N)
    # i = int(x * M) + 1  # i是一个整数，从0-N
    # k = float(i)
    # if (x == 1):
    #     x1 = x - 1 / (100 * M)
    # elif (i == x * M + 1):
    #     x1 = x + 1 / (100 * M)
    # elif (i % 2 == 1):
    #     x1 = M * M * U * (x - (k - 1) / M) * (k / M - x)
    # else:
    #     x1 = 1 - M * M * U * (x - (k - 1) / M) * (k / M - x)
    x1=U*x*(1-x)
    return x1


if __name__ == '__main__':
    listu=[]
    listx=[]
    for u in np.arange(0, 4.01, 0.01):
        x = 0.123456789
        print(u)
        for i in range(1, 500):
            x1 = PLM(u,x)
            x=x1
            if i > 150:
                listu.append(u)
                listx.append(x)


    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('N=64')
    # 设置X轴标签
    plt.xlabel('μ')
    # 设置Y轴标签
    plt.ylabel('Xn')

    # plt.grid(True, linestyle="-.", color="r", linewidth="3")
    ax1.scatter(listu, listx, c='b', marker='.', s=1)
    plt.show()
