import numpy as np


def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist


a = (0, 1, 1, 1, 2, 3, 7, 7, 23)
counted = count_elements(a)
# print(counted) # {0: 1, 1: 3, 2: 1, 3: 1, 7: 2, 23: 1}

np.random.seed(444)     # 记录随机数
np.set_printoptions(precision=3)    # 设置精度
# Laplace分布的概率密度函数: p(x) = 1/(2*λ)*exp(-fabs(x-μ)/λ)
# 源码函数：g = (1/(scale * np.sqrt(2 * np.pi)) *
#               p.exp(-(x - loc)**2 / (2 * scale**2)))
# loc：就是上面的μ，控制偏移。
# scale： 就是上面的λ，控制缩放。
# size：  是产生数据的个数
d = np.random.laplace(loc=15,scale=3,size=500)
# print(d[:5]) # [18.406 18.087 16.004 16.221  7.358]
hist,bin_edges = np.histogram(d)    # 频数，分箱的边界
# print(hist,bin_edges)
# [ 13  23  91 261  80  21   7   2   1   1]
# [ 2.11   5.874  9.638 13.402 17.166 20.93  24.694 28.458 32.222 35.986 39.749]
# 边界的数量是要比分箱数多一个
# print(hist.size,bin_edges.size) # 10 11

# 取a的最小值和最大值
first_edge, last_edge = min(a), max(a)
n_equal_bins = 10 # NumPy得默认设置，10个分箱
bin_edges = np.linspace(start=first_edge, stop=last_edge,
                        num=n_equal_bins + 1, endpoint=True)
# print(bin_edges)    # [ 0.   2.3  4.6  6.9  9.2 11.5 13.8 16.1 18.4 20.7 23. ]

import matplotlib.pyplot as plt
# matplotlib.axes.Axes.hist() 方法的接口
# n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
#                             alpha=0.7, rwidth=0.85) # rwidth= :柱子与柱子之间的距离，默认是0
# # print(n, bins, patches)
# plt.grid(axis='y', alpha=0.75) # alpha 频率分布图的透明度
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('My Very Own Histogram')
# plt.text(23, 45, r'$μ=15, λ=3$')
# maxfreq = max(n)# 设置y轴的上限
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# print(maxfreq,np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# plt.show()

import pandas as pd
# size, scale = 1000, 10
# commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)
# commutes.plot.hist(grid=True, bins=20, rwidth=0.9, color='#627a8a')
# plt.title('Commute Times for 1,000 Commuters')
# plt.xlabel('Counts')
# plt.ylabel('Commute Time')
# plt.grid(axis='y', alpha=0.75)  # 网格
# plt.show()

