from math import sqrt,log
import numpy as np


def cosine_similarity(A,B):
    sum1=0;sum2=0;sum3=0
    for i in range(0,len(A)):
        if(A[i]!=0 and B[i] != 0):
            sum1 += A[i]*B[i]
            sum2 += A[i]**2
            sum3 += B[i]**2
    if sum1 != 0:
        return sum1/(sqrt(sum2)*sqrt(sum3))
    else:
        return 0


def cos_output(U):
    print('\t',end='')
    for i in range(0,len(U)):
        print("  U%d\t"%(i+1),end='')
    print()
    for i in range(0,len(U)):
        print("U%d\t" % (i + 1), end='')
        for j in range(0,len(U)):
            sim = cosine_similarity(U[i], U[j])
            if i == j:
                print("  -  \t",end='')
            elif sim == 0:
                print("  *  \t", end='')
            else:
                print("%.3f\t" % sim,end='')
        print()


def kl_sim_l(I,J):
    r_max = 5;D_ij=0;D_ji=0;sign_i=0;sign_j=0;Ds=0;sim=0
    for i in range(0,len(I)):
        if I[i] != 0:
            sign_i += 1
    for i in range(0,len(J)):
        if J[i] != 0:
            sign_j += 1
    # print(sign_i,sign_j)
    for i in range(1,r_max+1):
        sign_r = 0
        for j in range(0,len(I)):
            if I[j] == i:
                sign_r += 1
        p_ir = sign_r/sign_i;sign_r=0
        if p_ir == 0:
            p_ir = 0.5/(1+0.5*r_max)
        for j in range(0,len(J)):
            if J[j] == i:
                sign_r += 1
        p_jr = sign_r/sign_j
        if p_jr == 0:
            p_jr = 0.5/(1+0.5*r_max)
        # print(p_ir,p_jr)
        D_ij += p_ir * log(p_ir/p_jr,2)
        D_ji += p_jr * log(p_jr/p_ir, 2)
        Ds = (D_ij+D_ji)/2
    L = 1/(1+Ds)
    return L


def save_sim_l(U):
    Ut = np.transpose(U)
    #print(Ut)
    Ul = [];l=[]
    for i in range(0,len(Ut)):
        for j in range(0,len(Ut)):
            sim_l = round(kl_sim_l(Ut[i],Ut[j]),3)
            l.append(sim_l)
        #print(l)
        Ul.append(l)
        l = []
    output_sim_l(Ul)


def output_sim_l(U):
    print('\t', end='')
    for i in range(0, len(U)):
        print("  I%d\t" % (i + 1), end='')
    print()
    for i in range(0, len(U)):
        print("I%d\t" % (i + 1), end='')
        for j in range(0, len(U)):
            sim = cosine_similarity(U[i], U[j])
            if i == j:
                print("  -  \t", end='')
            else:
                print("%.3f\t" % U[i][j], end='')
        print()


def main():
    U = [
            [4, 4, 0, 0, 0, 0],
            [0, 0, 4, 4, 3, 3],
            [4, 4, 5, 5, 3, 3],
            [2, 1, 2, 0, 1, 0],
            [0, 5, 0, 0, 1, 0],
    ]
    # U = np.transpose(U)
    # cos_output(U)
    save_sim_l(U)





if __name__ == '__main__':
    main()