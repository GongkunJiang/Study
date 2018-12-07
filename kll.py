import numpy as np
import scipy.stats
p = np.asarray([0,1/3,0,1/3,1/3])
# q = p
q = np.asarray([0,0,1,0,0])
p = (p+10**(-5))/(1+5*10**(-5))
q = (q+10**(-5))/(1+5*10**(-5))

# p = np.asarray([ 0 ,     0.01456311,  0.01456311,  0.04854369 , 0.00970874 , 0.17475728, 0.10679612 , 0.32524272,  0.08252427 , 0.22330097] )
# q = np.asarray([ 0   ,    0 ,          0  ,        0.16666667 , 0  ,         0.38888889 , 0    ,      0.27777778 , 0    ,       0.16666667])

# m = p+q
# temp1 = float(sum(p))
# temp2 = float(sum(q))
# temp3 = float(sum(m))

# p = p / temp1
# q =q / temp2
# M = m / temp3

print(p,'\n',q,'\n')
# # q = np.array([0.6, 0.25, 0.1, 0.05])
# m = (p+q)/2
# # 方法一：根据公式求解

kl1 =0.5*(scipy.stats.entropy(p, q)+ scipy.stats.entropy(q, p))
sim1 = 1/(1+kl1)
# # 方法二：调用scipy包求解
# kl2 = 0.5*(scipy.stats.entropy(q, M)+scipy.stats.entropy(p, M))
# sim2 = 1/(1+kl2)

# kl1:	 10.963091165827887
# sim1:	 0.08359043546006419
print('kl1:\t',kl1,'\nsim1:\t',sim1)