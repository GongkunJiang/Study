import numpy as np
import math
import matplotlib.pyplot as plt


def noisyCount(sensitivety, epsilon):
    beta = sensitivety / epsilon
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        n_value = -beta * np.log(1. - u2)
    else:
        n_value = beta * np.log(u2)
    # print(n_value)
    return n_value


def laplace_mech(data, sensitivety, epsilon):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] += noisyCount(sensitivety, epsilon)
    return data


if __name__ == '__main__':
    sensitivety = 1
    epsilon = np.linspace(0.01, 1, 100)
    data = [noisyCount(sensitivety, epsilon_) for epsilon_ in epsilon]
    plt.plot(epsilon, data, color='k', label='epsilon:(0.01,1, 100)')
    plt.title("epsilon = np.linspace(0.01,1, 100)")
    plt.legend()
    plt.show()

    # loc, scale = 0., 1.
    s = np.random.laplace(loc, scale, 1000)
    # result_list = list(map(lambda x: x + 50, s))
    # plt.hist(result_list, 30)
    # plt.show()