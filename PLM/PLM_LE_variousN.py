from sympy import *
import numpy as np
np.set_printoptions(suppress=True)
import matplotlib.pyplot as plt


# 4.57459433028122

U = 4
global N
def PLM(x,n):
    for z in range(n):
        M=float(N)
        i=int(x*M)+1#i是一个整数，从0-N
        k=float(i)
        if(x==1):
            x1=x-1/(100*M)
        elif (i==x*M+1):
            x1=x+1/(100*M)
        elif(i%2==1):
            x1=M*M*U*(x-(k-1)/M)*(k/M-x)
        else:
            x1=1-M*M*U*(x-(k-1)/M)*(k/M-x)
        x=x1
        # print(x)
    return x

def Jacobian(a):
    x = symbols('x')
    M = float(N)
    i = int(a * M) + 1
    k = float(i)
    expr1 = x - 1 / (100 * M)
    expr2 = x + 1 / (100 * M)
    expr3 = M * M * U * (x - (k - 1) / M) * (k / M - x)
    expr4 = 1 - M * M * U * (x - (k - 1) / M) * (k / M - x)

    if (a == 1):
        expr = expr1
    elif (i == a * M + 1):
        expr = expr2
    elif (i % 2 == 1):
        expr = expr3
    else:
        expr = expr4
    f_mat = Matrix([expr])
    jacobi_mat = f_mat.jacobian([x])
    return jacobi_mat


def LE_calculate(a,n=5000):
    sum_Lambda1 = 0
    # 使用符号方式求解
    x = symbols("x")
    a = PLM(a, 100)  # 先迭代100次，消除初始影响.以第5001次的值作为初始值
    U1 = Matrix([1])  # 初始列向量
    for i in range(n):
        jacobi_mat=Jacobian(a)
        J = jacobi_mat.subs(x, a)  # 将变量替换为当前迭代值，得到当前的雅各比矩阵（数字）
        column_vector1 = U1  # 初始列向量为上一次的U1
        vector1 = J * column_vector1  # 初始列向量乘上雅各比矩阵之后得到的向量
        V1 = vector1  # 将vector1复制给V1
        U1 = V1 / (V1.norm(2))  # 向量U1等于向量V1除以向量V1的模(2范数)
        Lambda1 = ln(V1.norm(2))
        sum_Lambda1 = sum_Lambda1 + Lambda1
        a = PLM(a, 1)  # 进行下一次迭代
        # print(i)
    LE1 = sum_Lambda1 / n
    # print(LE1)
    return LE1



if __name__ == '__main__':
    global N
    LElist=[]
    Nlist=[]
    for i in range(1,101):
        print(i)
        N=i
        LE=LE_calculate(0.123456789)
        LElist.append(LE)
        Nlist.append(N)
    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('μ=4')
    # 设置X轴标签
    plt.xlabel('N')
    # 设置Y轴标签
    plt.ylabel('Lyapunov exponent')
    plt.grid(True,linestyle='dotted')
    plt.xlim(0, 100)
    plt.ylim(-4, 6)
    plt.plot(Nlist,LElist, c='b', linewidth=1)
    plt.show()