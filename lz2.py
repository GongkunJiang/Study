from sympy import *
import matplotlib.pyplot as plt
import random

def PLM(x):
    U = 0.5
    N = 8
    list_x = []
    # for z in range(n):
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
    # list_x.append(x)
    return x1

def Two_Dimensional_Coupled_Map_Lattice():
    E = 0.1
    R = 8
    L = 8
    iterations = 2000
    Lattice = []
    # Convert = np.zeros(iterations)
    Convert = []
    x=[]
    # print(Convert)
    for i in range(R):
        temp = []
        for j in range(L):
            temp.append(random.random())
        # print(temp)
        Lattice.append(temp)
    for k in range(iterations):
        coupled = EOFError
        for i in range(R):
            for j in range(L):
                self = Lattice[1][1]
                up = Lattice[(1 - 1) % R][1]
                down = Lattice[(1 + 1) % R][1]
                left = Lattice[1][(1 - 1) % L]
                right = Lattice[1][(1 + 1) % L]
                coupled = (1 - E) * PLM(self) + (E / 4) * (PLM(up) + PLM(down) + PLM(left) + PLM(right))
                # if coupled > 1:
                #     coupled = coupled - 1
                Lattice[i][j] = coupled
                # Convert[k]= coupled
                Convert.append(coupled)
                x.append(k*64+ i*8+j)
                print(k,i,j,coupled)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('N=2', fontsize='16')
    plt.xlabel('μ', fontsize='16')
    plt.ylabel('Lyapunov exponent', fontsize='16')
    plt.grid(True, linestyle='dotted')
    plt.xlim(0, 2000)
    plt.ylim(0, 1)
    plt.plot(x, Convert, c='b', linewidth=1)
    plt.show()

def main():
    Two_Dimensional_Coupled_Map_Lattice()


if __name__ == '__main__':
    main()