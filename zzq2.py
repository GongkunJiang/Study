import math as mt
import numpy as np
import matplotlib.pyplot as plt
import os

N = 0


def new_cubic(x):
    i = ((x+1)*N)/2
    if i != int(i):
        i = mt.ceil((((x + 1) * N) / 2))
    else:
        i = int(i+1)
    x1=4*(N*x+N+1-2*i)**3-3*(N*x+N+1-2*i)
    x=x1
    return x


def draw():
    print('Start draw . . .\n')
    listx = []
    listy = []
    step = 100000
    j = 0
    path = 'E:\JetBrains\code\zzq2_data.txt'
    if os.path.exists(path):
        os.remove(path)
    for i in np.arange(-1, 1, 1 / step):
        i = round(i, len(str(step)))
        listx.append(i)
        y = new_cubic(i)
        listy.append(y)
        print(j)
        with open(path, 'a+') as f:
            f.write(str(j)+'\t'+str(i)+'\t'+str(y))
            f.write('\n')
        j += 1
    count = 2 * step / N
    start = 0
    end = mt.ceil(count)
    for k in range(N):

        print(k+1, start, end, len(listy[start:end]))
        plt.plot(listx[start:end], listy[start:end])
        start = end
        end = mt.ceil((k + 2) * count)
    plt.show()
    print('\ndraw done !!!')


if __name__ == '__main__':
        for N in [64]:
            plt.figure()
            plt.title('N=%s'%N)
            plt.xlim(-1, 1)
            plt.ylim(-1, 1)
            plt.xlabel('x')
            plt.ylabel('y')
            draw()

