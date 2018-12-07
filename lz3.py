import matplotlib.pyplot as plt
import numpy as np
import random


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


E, R, L = 0.1, 8, 8

Lattice = []
for i in range(R):
    temp = []
    for j in range(L):
        temp.append(random.random())
    Lattice.append(temp)

x, data = [], []
#
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
# plt.title('lattice (1,1) varies with the probability')
# plt.xlabel('μ')
# plt.ylabel('x_n')
# plt.xlim(0, 4)
# plt.ylim(0, 1)


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
# plt.title('The bifurcation graph of lattice (1,1) varies with N')
# plt.xlabel('N')
# plt.ylabel('x_n')
# plt.xlim(0, 1000)
# plt.ylim(0, 1)

k, N = 0.5, 2  # 3254.pdf 图2
for n in range(1, 1101):
    print(n)
    for i in range(R):
        for j in range(L):
            self = Lattice[i][j]
            up = Lattice[(i - 1) % R][j]
            down = Lattice[(i + 1) % R][j]
            left = Lattice[i][(j - 1) % L]
            right = Lattice[i][(j + 1) % L]
            Lattice[i][j] = (1 - E) * PLM(k, N, self) + (E / 4) * \
                            (PLM(k, N, up) + PLM(k, N, down) + PLM(k, N, left) + PLM(k, N, right))

            if n > 100:
                x.append(n - 100)
                data.append(Lattice[i][j])
plt.title('μ = %s, N = %s' % (k, N))
plt.xlabel('n')
plt.ylabel('x_n')
plt.xlim(0, 1000)
plt.ylim(0, 1)

# k, N_list, = 4, [2, 8, 32, 64]  # 3254.pdf 图3
# line_style, colour = ['-', '--', ':', '-.'], ['b', 'r', 'k', 'm']
# for N in N_list:
#     index = N_list.index(N)
#     for n in range(1, 1101):
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
#     hist, bin_edges = np.histogram(data, 100)
#     iterations = len(data)
#     plt.plot([(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(hist))],
#              hist / iterations, line_style[index], color=colour[index], label='N = %d' % N)
# plt.legend(loc='upper center')
# plt.title('probability density distribution changes with respect to N')
# plt.xlabel('x')
# plt.ylabel('frequency')
# plt.xlim(0, 1)
# plt.ylim(0, 2.5 * (10 ** (-2)))

plt.scatter(x, data, c='b', marker='.')
plt.show()
