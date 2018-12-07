import matplotlib.pyplot as plt
import numpy as np
from final_exam_2 import b2_x
import math,sympy


def PLM_diff(N,k,x0):
    y = EOFError
    if x0 == 1 or x0 % (1 / N) == 0:
        y = 1
    elif 0 < x0 < 1 / N:
        y = N*k - 2*k*(N**2)*x0

    else:
        for j in range(1, N):
            if j % 2 == 1 and j / N < x0 < (j + 1) / N:
                y = k*(N**2)*(2*x0 - (2*j+1)/N)
            elif j % 2 == 0 and j / N < x0 < (j + 1) / N:
                y = -k*(N**2)*(2*x0 - (2*j+1)/N)
    return y


def PLM(N,k,x0):
    y = EOFError
    if x0 == 1:
        y = x0 - 1 / (100 * N)
    elif x0 % (1 / N) == 0:
        y = x0 + 1 / (100 * N)
    elif 0 < x0 < 1 / N:
        y = k * (N ** 2) * x0 * (1 / N - x0)

    else:
        for j in range(1, N):
            if j % 2 == 1 and j / N < x0 < (j + 1) / N:
                y = 1 - k * (N ** 2) * (x0 - j / N) * ((j + 1) / N - x0)
            elif j % 2 == 0 and j / N < x0 < (j + 1) / N:
                y = k * (N ** 2) * (x0 - j / N) * ((j + 1) / N - x0)
    return y


def bifurcation_diagram():
    # x0 = np.random.random()
    x0 = 0.3114680394046133
    list_N = [2,8,16,20,32,64]
    for N in list_N:
        list_k = []
        list_x = []
        print(x0)
        for k in np.linspace(0.01, 4, 400):
            print(k)
            for i in range(1, 501):
                # x0 = PLM(N, k, x0)
                x = PLM(N,k,x0)
                x0 = b2_x(x)
                if i > 150:
                    list_k.append(k)
                    list_x.append(x0)
        plt.plot(list_k, list_x, marker=',', linestyle='' '', color='b')
        plt.xlabel('k')
        plt.ylabel('x_n')
        plt.xlim(0, 4)
        plt.ylim(0, 1)
        # title = 'PLM Bifurcation Diagram N=%s' % N
        title = 'PLM nested Bifurcation Diagram N=%s' % N
        plt.title(title)
        fig = plt.gcf()
        plt.show()
        fig.savefig(r'E:\JetBrains\data_fig\%s.png' % title)


def lyapunov_exponent():
    # x0 = np.random.random()
    x0 = 0.3114680394046133
    k = 1.01
    list_k = []
    list_x = []
    lyp = 0
    for N in range(1,10):
        for i in range(1,10001):
            lyp += math.log(math.fabs(PLM_diff(N,k,x0)),math.e)
            x0 = b2_x(PLM(N,k,x0))
        lyp = lyp/10000
        list_x.append(lyp)
        list_k.append(N)
        print(N,lyp)

    plt.plot(list_k, list_x, marker='o', linestyle='-', color='b')
    plt.xlabel('k')
    plt.ylabel('x_n')
    # title = 'PLM Bifurcation Diagram N=%s' % N
    title = 'PLM nested Bifurcation Diagram k=%s' % str(k)
    plt.title(title)
    fig = plt.gcf()
    plt.grid(True, linestyle=":",axis='y')
    plt.show()
    fig.savefig(r'E:\JetBrains\data_fig\%s.png' % title)


def main():
    # bifurcation_diagram()
    # lyapunov_exponent()
    pass

if __name__ == '__main__':
    main()