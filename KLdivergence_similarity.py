from fractions import Fraction
from math import log
from numpy import transpose,zeros


def kl_output(U,type):
    if type == 'user':
        T = 'U'
    elif type == 'item':
        T = 'I'
        U = transpose(U)
    else:
        T = 'error'
    sim = zeros((len(U), len(U)))
    # print('\t',end='')
    # for i in range(len(U)):
    #     print("  %s%d\t"%(T,(i+1)),end='')
    # print()
    for i in range(len(U)):
        # print("%s%d\t" % (T,(i+1)), end='')
        for j in range(len(U)):
            effective_score_numi = effective_score_num(U[i])
            effective_score_numj = effective_score_num(U[j])
            scores_total = 5
            Di = density_function(U[i],scores_total,effective_score_numi)
            Dj = density_function(U[j],scores_total,effective_score_numj)
            Si = smoothing(Di,scores_total)
            Sj = smoothing(Dj,scores_total)
            sim[i][j] = kldivergence_similarity(Si, Sj)
        #     if i == j:
        #         print("  -  \t",end='')
        #     elif sim == 0:
        #         print("  *  \t", end='')
        #     else:
        #         print("%.3f\t" % sim,end='')
        # print()
    return sim

def kldivergence_similarity(I,J):
    D_ij=0;D_ji=0
    for k in range(len(I)):
        D_ij += I[k] * log(I[k]/J[k],2)
        D_ji += J[k] * log(J[k]/I[k],2)
    Ds = (D_ij+D_ji)/2
    L = 1/(1+Ds)
    return L


def effective_score_num(M):
    num = 0
    for i in range(len(M)):
        if M[i] != 0:
            num += 1
    return num


def density_function(M,scores_total,effective_score_num):
    Density =zeros(scores_total)
    for i in range(len(M)):
        for j in range(1,scores_total+1):
            if M[i] == j:
                Density[j-1] += Fraction(1,effective_score_num)
    return Density


def smoothing(D,scores_total):
    S = zeros(scores_total)
    zero = False
    for i in range(len(D)):
        if D[i] == 0:
            zero = True
    if not zero :
        return D
    else:
        deta = 10**(-5)
        for i in range(len(S)):
            S[i] = (D[i]+deta)/(1+deta*scores_total)
        return S


def main():
    U = eval(input("Please enter User-Item scoring matrix:\n"))
    for type in ['user','item']:
        print('\n\n kldivergence_similarity--%s'%type)
        kl_output(U, type)
    # U = [
    #     [4, 4, 0, 0, 0, 0],
    #     [0, 0, 4, 4, 3, 3],
    #     [4, 4, 5, 5, 3, 3],
    #     [2, 1, 2, 0, 1, 0],
    #     [0, 5, 0, 0, 1, 0],
    # ]
    # Ut = transpose(U)
    # effective_score_num3 = effective_score_num(Ut[2]) # 3
    # effective_score_num6 = effective_score_num(Ut[5])   # 2
    # scores_total = 5
    # D3 = density_function(Ut[2],scores_total,effective_score_num3)  # [0.         0.33333333 0.         0.33333333 0.33333333]
    # D6 = density_function(Ut[5],scores_total,effective_score_num6)  #  [0. 0. 1. 0. 0.]
    # S3 = smoothing(D3,scores_total) # [9.99950002e-06 3.33326667e-01 9.99950002e-06 3.33326667e-01 3.33326667e-01]
    # S6 = smoothing(D6,scores_total) # [9.99950002e-06 9.99950002e-06 9.99960002e-01 9.99950002e-06 9.99950002e-06]
    # s36 = kldivergence_similarity(S3, S6)   # (15.8163972577535, 0.05946576931268272)
    # print(s36)


if __name__ == '__main__':
    main()