from math import sqrt,copysign,log,fabs
from numpy import transpose,zeros,linspace
import LaplaceNoise,KLdivergence_similarity
import matplotlib.pyplot as plt

def cosine_similarity(A,B):
    sum1=0;sum2=0;sum3=0
    for i in range(len(A)):
        if(A[i]!=0 and B[i] != 0):
            sum1 += A[i]*B[i]
            sum2 += A[i]**2
            sum3 += B[i]**2
    if sum1 != 0:
        return sum1/(sqrt(sum2)*sqrt(sum3))
    else:
        return 0


def cos_output(U,type):
    if type == 'user':
        T = 'U'
    elif type == 'item':
        T = 'I'
        U = transpose(U)
    else:
        T = 'error'
    sim = zeros((len(U),len(U)))
    # print('\t',end='')
    # for i in range(len(U)):
    #     print("  %s%d\t"%(T,(i+1)),end='')
    # print()
    for i in range(len(U)):
        # print("%s%d\t" % (T,(i+1)), end='')
        for j in range(len(U)):
            sim[i][j] = cosine_similarity(U[i], U[j])
        #     if i == j:
        #         print("  -  \t",end='')
        #     elif sim[i][j] == 0:
        #         print("  *  \t", end='')
        #     else:
        #         print("%.3f\t" % sim[i][j],end='')
        # print()
    return sim


def noise_similarity(sim,U):
    x=2;y=3;mu = 0
    b = linspace(0.1, 1, 10)
    sim_final = zeros(len(b))
    for i in range(len(b)):
        noise = LaplaceNoise.addnoise(U, mu, b[i])
        sim_noise = cos_output(noise,'user')
        sim_final[i] = 1 - fabs(sim[x-1][y-1] - sim_noise[x-1][y-1])/sim[x-1][y-1]
        print(sim[x-1][y-1],sim_noise[x-1][y-1],sim_final[i])
    # return sim_final
    # Unoise = [LaplaceNoise.addnoise(U, mu, b_) for b_ in b]
    # Usim = [cos_output(Unoise_, 'user') for Unoise_ in Unoise]

    plt.plot(b, sim_final, color='r', label='x=2;y=3;mu=0')
    plt.title("Anti-noise Capacity")
    plt.legend()
    plt.show()

def main():
    U = [
            [4, 4, 0, 0, 0, 0],
            [0, 0, 4, 4, 3, 3],
            [4, 4, 5, 5, 3, 3],
            [2, 1, 2, 0, 1, 0],
            [0, 5, 0, 0, 1, 0],
    ]
    type = 'user'
    cos_prime_sim = cos_output(U, type)
    # print (sim[1][2])
    cos_noise_sim = noise_similarity(cos_prime_sim,U)
    # kl_prime_sim = KLdivergence_similarity.kl_output(U,type)
    # print(kl_prime_sim)
    # kl_noise_sim = noise_similarity(kl_prime_sim,U)
    # print(noise_sim)
    # U = eval(input("Please enter User-Item scoring matrix:\n"))
    # type = input("Please choose the type('user' or 'item'):\n")
    # cos_output(U,type)
    # for type in ['user','item']:
        # print('\n\n cosine_similarity--%s'%type)
        # sim = cos_output(U, type)
    # mu = 0
    # b = 10 ** (-1)
    # Unoise = Laplace_mechanism.laplace_mech(sim, sensitivety, epsilon)
    # Unoise = LaplaceNoise.addnoise(U, mu, b)
    # print(Unoise)

if __name__ == '__main__':
    main()