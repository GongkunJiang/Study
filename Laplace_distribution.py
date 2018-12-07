import matplotlib.pyplot as plt
import numpy as np
import bit_switch


def laplace_function(x, beta):
    result = (1 / (2 * beta)) * np.e ** (-1 * (np.abs(x) / beta))
    return result


# 在-5到5之间等间隔的取10000个数
x = np.linspace(-5, 5, 10000)
y1 = [laplace_function(x_, 0.5) for x_ in x]
y2 = [laplace_function(x_, 1) for x_ in x]
y3 = [laplace_function(x_, 2) for x_ in x]
y4 = [laplace_function(x_, 3) for x_ in x]

plt.plot(x, y1, color='r', label='beta:0.5')
plt.plot(x, y2, color='g', label='beta:1')
plt.plot(x, y3, color='b', label='beta:2')
plt.plot(x, y4, color='k', label='beta:2')
plt.title("Laplace distribution")
plt.legend()
plt.show()

# np.random.laplace可以获得拉普拉斯分布的随机值，参数主要如下：
# loc：就是上面的μ，控制偏移。
# scale： 就是上面的λ,控制缩放。
# size：  是产生数据的个数
