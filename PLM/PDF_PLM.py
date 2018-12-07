from sympy import *
import matplotlib.pyplot as plt

def PLM(x,n):
    U = 4.0
    N = 64
    list_x = []
    for z in range(n):
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

        x=x1
        list_x.append(x)
    return list_x


if __name__ == '__main__':
    list_x=PLM(0.15626359235822565,100000)
    plt.hist(list_x, bins=1000, color='steelblue')
    plt.show()