import bit_switch
import numpy as np
import math,random
import matplotlib.pyplot as plt
import pandas as pd
import double_precision,bit_switch


def logistic_map(k,x,iterations):
    result = []
    for i in range(iterations):
        # x1 = k*x*(1-x)

        x1 = 1 - k*x**2
        x=x1
        result.append(x)
    return result


def p_xn(logist):
    result = []
    for i in range(len(logist)):
        result.append(1/(math.pi*math.sqrt(1-logist[i]**2)))
    return result


def thita(logist):
    result = []
    for i in range(len(logist)):
        result.append(1 / (math.acos(logist[i])/math.pi))
    return result

def main():
    x0 = -1 + 2*random.random()
    print(x0)
    # x0 = 0.3345
    k = 2
    logist = logistic_map(k,x0,100000)
    # Thita = thita(logist)
    # P_xn = p_xn(Thita)
    # print(logist,'\n',Thita,'\n',P_xn)
    hist, bin_edges = np.histogram(logist,100)
    # print(hist,'\n',bin_edges)
    # n, bins, patches = plt.hist(x=logist, bins=100, color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('homogenize_logistic')
    for i in range(len(hist)):
        plt.scatter((bin_edges[i]+bin_edges[i+1])/2, hist[i], s=10, c="b", marker=',')
    print(len(hist),len(bin_edges)) # 100 101

    homo = []
    for i in range(len(logist)):
        homo.append(bit_switch.b2_x(logist[i]))
    hist2, bin_edges2 = np.histogram(homo, 10)
    for i in range(len(hist2)):
        plt.scatter((bin_edges[i]+bin_edges[i+1])/2, hist2[i], s=10, c="r", marker='x')
    # print(homo)
    # print(hist2, bin_edges2)
    plt.show()


if __name__ == '__main__':
    main()