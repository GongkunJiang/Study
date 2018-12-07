from numpy import zeros,linspace
import pandas as pd
import math, random
import matplotlib.pyplot as plt


# mu一般取0，b=Δf/ epsilon
def getnoise(mu, b):
    alpha = random.random() - 0.5
    noise = mu - math.copysign(b, alpha) * math.log(1 - 2 * math.fabs(alpha))
    return noise


# print(getnoise(0,1))


def addnoise(data, sensitivety, epsilon):

    # deltaf = np.max(np.sum(np.abs(train_x), axis=1))    #axis=1时就是将一个矩阵的每一行向量相加
    # lambd = deltaf / epsilon
    # data_raw['noiserating'] = data_raw['rating'] + getnoise(0, 1)
    for i in range(len(data)):
        # for j in range(len(data[i])):
        data[i] += getnoise(sensitivety, epsilon)
    return data


if __name__ == '__main__':
    # noise = zeros(10)
    # print(noise)
    # b = linspace(0.01, 1, 10)
    # for i in range(len(b)):
    #     noise = addnoise(noise,0,b[i])
    #     print(noise[5])
    # plt.plot(b, noise, color='b', label='b = linspace(0.01, 1, 10)')
    # plt.title("LaplaceNoise")
    # # plt.legend()
    # plt.show()
    sensitivety = 1
    epsilon = linspace(0.01, 1, 100)
    data = [getnoise(sensitivety, epsilon_) for epsilon_ in epsilon]
    print(data)
    plt.plot(epsilon, data, color='k', label='epsilon:(0.01,1, 100)')
    plt.title("epsilon = np.linspace(0.01,1, 100)")
    plt.legend()
    plt.show()