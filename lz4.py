import matplotlib.pyplot as plt
import numpy as np
import random
from final_exam_2 import b2_x


def PLM(k, N, x):
    y = EOFError
    if x == 1:
        y = x - 1 / (100 * N)
    elif x % (1 / N) == 0:
        y = x + 1 / (100 * N)
    elif 0 < x < 1 / N:
        y = k * (N ** 2) * x * (1 / N - x)

    else:
        j = int(x * N)  # 直接判断x落在区间的第几段
        if j % 2 == 1 and j / N < x < (j + 1) / N:
            y = 1 - k * (N ** 2) * (x - j / N) * ((j + 1) / N - x)
        elif j % 2 == 0 and j / N < x < (j + 1) / N:
            y = k * (N ** 2) * (x - j / N) * ((j + 1) / N - x)
    return y




# for K in range(1, 4001): # 3254.pdf 图1(a)
#     k, N = K / 1000, 64
#     print(k)
#     for it in range(200):
#         for i in range(R):
#             for j in range(L):
#                 self = Lattice[i][j]
#                 up = Lattice[(i - 1) % R][j]
#                 down = Lattice[(i + 1) % R][j]
#                 left = Lattice[i][(j - 1) % L]
#                 right = Lattice[i][(j + 1) % L]
#                 Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
#                                 (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))
#                 if it > 100 and i == j == 0:
#                     x.append(k)
#                     data.append(Lattice[i][j])
# # plt.title('lattice (1,1) varies with the probability')
# plt.xlabel('$μ$',fontsize=20)
# plt.ylabel(r"$x_{n}$",fontsize=20)
# plt.xlim(0, 4)
# plt.ylim(0, 1)
# plt.tick_params(labelsize=20)
#
# for N in range(1, 1001, 1):  # 3254.pdf 图1(b)
#     k = 4
#     print(N)
#     for it in range(200):
#         for i in range(R):
#             for j in range(L):
#                 self = Lattice[i][j]
#                 up = Lattice[(i - 1) % R][j]
#                 down = Lattice[(i + 1) % R][j]
#                 left = Lattice[i][(j - 1) % L]
#                 right = Lattice[i][(j + 1) % L]
#                 Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
#                                 (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))
#                 if it > 100 and i == j == 0:
#                     x.append(N)
#                     data.append(Lattice[i][j])
# # plt.title('The bifurcation graph of lattice (1,1) varies with N')
# plt.xlabel('$N$',fontsize=20)
# plt.ylabel(r"$x_{n}$,fontsize=20)
# plt.xlim(0, 1000)
# plt.ylim(0, 1)
# plt.tick_params(labelsize=20)

# k, N = 4,32# 3254.pdf 图2
# for n in range(1, 1101):
#     print(n)
#     for i in range(R):
#         for j in range(L):
#             self = Lattice[i][j]
#             up = Lattice[(i - 1) % R][j]
#             down = Lattice[(i + 1) % R][j]
#             left = Lattice[i][(j - 1) % L]
#             right = Lattice[i][(j + 1) % L]
#             Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
#                             (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))
#
#             if n > 100:
#                 x.append(n - 100)
#                 data.append(Lattice[i][j])
# plt.title('$μ$ = %s, $N$ = %s' % (k, N),fontsize=20)
# plt.xlabel('$n$',fontsize=20)
# plt.ylabel('r"$x_{n}$"',fontsize=20)
# plt.xlim(0, 1000)
# plt.ylim(0, 1)
# plt.tick_params(labelsize=18)

# k, N = 2,32 # 遍历轨道
# for n in range(1, 10101):
#     print(n)
#     for i in range(R):
#         for j in range(L):
#             self = Lattice[i][j]
#             x.append(self)
#             up = Lattice[(i - 1) % R][j]
#             down = Lattice[(i + 1) % R][j]
#             left = Lattice[i][(j - 1) % L]
#             right = Lattice[i][(j + 1) % L]
#             Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
#                             (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))
#
#             # if n > 100:
#                 # x.append(n - 100)
#             data.append(Lattice[i][j])
# plt.title('$μ$ = %s, $N$ = %s' % (k, N),fontsize=20)
# plt.xlabel(r"$x_{n}$",fontsize=20)
# plt.ylabel(r"$x_{n+1}$",fontsize=20)
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.tick_params(labelsize=18)


# k, N_list, = 4, [2, 8, 32, 64]  # 概率密度图不均匀
# line_style, colour = ['-', '--', ':', '-.'], ['b', 'r', 'k', 'm']
# for N in N_list:
#     index = N_list.index(N)
#     for n in range(1, 100101):
#         print(index, n)
#         for i in range(R):
#             for j in range(L):
#                 self = Lattice[i][j]
#                 up = Lattice[(i - 1) % R][j]
#                 down = Lattice[(i + 1) % R][j]
#                 left = Lattice[i][(j - 1) % L]
#                 right = Lattice[i][(j + 1) % L]
#                 Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
#                                 (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))
#                 if n >=100:
#                     data.append(Lattice[i][j])
#     hist, bin_edges = np.histogram(data, 1000)
#     iterations = len(data)
#     plt.plot([(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(hist))],
#              hist / iterations, line_style[index], color=colour[index], label='N = %d' % N)
# plt.legend(loc='upper center',fontsize=18)
# # plt.title('probability density distribution changes with respect to N',fontsize=20)
# plt.xlabel('$x$',fontsize=20)
# plt.ylabel('frequency',fontsize=20)
# plt.xlim(0, 1)
# plt.ylim(0, 2.5 * (10 ** (-3)))
# plt.tick_params(labelsize=18)

# k, N_list, = 4, [2, 8, 32, 64]  # 概率密度图均匀
# line_style, colour = ['-', '--', ':', '-.'], ['b', 'r', 'k', 'm']
N=64
k=4
# for N in N_list:
#     index = N_list.index(N)
for time in range(2):
    E, R, L = 0.1, 8, 8

    Lattice = []
    for i in range(R):
        temp = []
        for j in range(L):
            temp.append(random.random())
        Lattice.append(temp)

    x, data = [], []
    for n in range(1, 1101):
        print(N, n)
        # a = [];b=[]
        for i in range(R):
            for j in range(L):
                self = Lattice[i][j]
                up = Lattice[(i - 1) % R][j]
                down = Lattice[(i + 1) % R][j]
                left = Lattice[i][(j - 1) % L]
                right = Lattice[i][(j + 1) % L]
                Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
                                (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))
                if time == 1:
                # a.append(Lattice[i][j])
                    Lattice[i][j]= b2_x( Lattice[i][j])
                # b.append(Lattice[i][j])
                # Lattice[i][j] = b2_x(Lattice[i][j])
                if n >= 100:
                    data.append(Lattice[i][j])
    hist, bin_edges = np.histogram(data, 1000)
    iterations = len(data)
    if time == 0:
        plt.plot([(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(hist))],
                 hist / iterations, '-', color='b', label='N = %d' % N)
    else:
        plt.plot([(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(hist))],
                 hist / iterations, '-', color='r', label='N = %d' % N)
    # plt.legend(loc='upper center',fontsize=15)

    plt.title('$N$ = %s' % (N), fontsize=20)
    # plt.title('probability density distribution changes with respect to N',fontsize=20)
    plt.xlabel('$x$', fontsize=20)
    plt.ylabel('frequency', fontsize=20)
    # plt.xlim(0, 1)
    # plt.ylim(0, 2.5 * (10 ** (-3)))
    plt.tick_params(labelsize=18)

    # plt.scatter(x, data, c='b', marker='.')
    # # plt.savefig('5555.png')
plt.show()
