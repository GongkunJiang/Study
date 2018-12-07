import random,math
import matplotlib.pyplot as plt


def get_noise(mu, b):
    # x=µ — b*sign(ksi')*ln(l — 2abs(ksi'))
    alpha = random.random() - 0.5
    noise = mu - math.copysign(b, alpha) * math.log(1 - 2 * math.fabs(alpha))
    return noise


laplace1 = [get_noise(0,1) for i in range(10000)]
laplace2 = [get_noise(0,2) for j in range(10000)]
laplace3 = [get_noise(0,0.5) for k in range(10000)]
laplace4 = [get_noise(0,1.5) for m in range(10000)]

fig, (ax1, ax2,ax3,ax4) = plt.subplots(1,4, sharex=False, sharey=True)
# bins : integer or array_like, optional
# 这个参数指定bin(箱子)的个数,也就是总共有几条条状图
ax1.hist(laplace1,bins=1000, label="b:1")
ax1.legend()
ax2.hist(laplace2, bins=1000, label="b:2")
ax2.legend()
ax3.hist(laplace3, bins=1000, label="b:0.5")
ax3.legend()
ax4.hist(laplace4, bins=1000, label="b:1.5")
ax4.legend()
plt.show()