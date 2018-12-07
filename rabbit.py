# static u32 RABBIT_g_func(u32 x)
# {
#    /* Temporary variables */
#    u32 a, b, h, l;
#
#    /* Construct high and low argument for squaring */
#    a = x&0xFFFF;
#    b = x>>16;
#
#    /* Calculate high and low result of squaring */
#    h = (((U32V(a*a)>>17) + U32V(a*b))>>15) + b*b;
#    l = x*x;
#
#    /* Return high XOR low */
#    return U32V(h^l);
# }


def bin_print(x):
    bin = ''
    while x > 0:
        if len(bin) != 0 and len(bin.replace(' ', '')) % 4 == 0:
            bin = ' ' + bin
        bin = str(x % 2) + bin
        x = int(x / 2)
    while len(bin.replace(' ', '')) < 64:
        if len(bin.replace(' ', '')) % 4 == 0:
            bin = ' ' + bin
        bin = '0' + bin
    print(bin)


x = 0XF0F0F0FF
l = x * x  # 0XE2C4A6A2E0FF1E01
m = l >> 32  # 0XE2C4A6A2
g = l ^ m  # 0XE2C4A6A2023BB8A3
g_m = g % (2 ** 32)  # 0X23BB8A3
a = x & 0xFFFF  # 0XF0FF
b = x >> 16  # 0XF0F0
h1 = (a * a) >> 17  # 0X716F
h2 = (h1+(a * b)) >> 15  # 0X1C5A2
h3 = b * b  # 0XE2C2E100
h = h2 +h3  # 0XE2C4A6A2
h_m = (h^l) % (2 ** 32)   # 0X23BB8A3
 

# print("%#X" % h_m)
# print("x\t:",end='');bin_print(x)
# print("l\t:",end='');bin_print(l)
# print("m\t:",end='');bin_print(m)
# print("g\t:",end='');bin_print(g)
# print("g_m\t:",end='');bin_print(g_m)
# print("a\t:",end='');bin_print(a)
# print("b\t:",end='');bin_print(b)
# print("h1\t:",end='');bin_print(h1)
# print("h2\t:",end='');bin_print(h2)
# print("h3\t:",end='');bin_print(h3)
# print("h\t:",end='');bin_print(h)
# print("h_m\t:",end='');bin_print(h_m)
bin_print(h1+(a * b))
