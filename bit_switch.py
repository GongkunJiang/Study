import bit_shift,double_precision


def reverse(string):
    return string[::-1]


def xor(s1,s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += '0'
        else:
            result += '1'
    return result


def define(f):
    # print(f)    # 0000000000000001010000111010000111101011010011001100
    f_H = f[:int(len(f)/2)]
    # print(f_H)  # 00000000000000010100001110
    f_L = f[int(len(f)/2):]
    # print(f_L)                            # 10000111101011010011001100
    f_Lr = reverse(f_L)
    # print(f_Lr) # 00110011001011010111100001
    f_Hr = xor(f_H,f_Lr)
    # print(f_Hr)     # 00110011001011000011101111
    Bit_f = f_Hr + f_L
    # print(Bit_f)  # 0011001100101100001110111110000111101011010011001100

    return f_H,f_L,f_Lr,f_Hr,Bit_f


# 第一类bit位变换
def b1_x(real_number):
    double_pre = double_precision.double_precision(real_number)
    # print(double_pre)   # ('0', '10000000101', '0000000000000001010000111010000111101011010011001100')
    Bit_f = define(double_pre[2])[4]            # 0011001100101100001110111110000111101011010011001100
    # print(Bit_f)
    return [double_pre[0],double_pre[1],Bit_f]


# 第二类bit位变换
def b2_x(real_number):
    double_pre = double_precision.double_precision(real_number)
    # print(double_pre)     # ('0', '10000000101', '0000000000000001010000111010000111101011010011001100')
    Bit_f = define(double_pre[2])[4]              # 0011001100101100001110111110000111101011010011001100
    # print(Bit_f)
    left_switch = bit_shift.left_bit_shift(Bit_f)
    # print(left_switch)
    # ('001', '1001100101100001110111110000111101011010011001100',
    # '1001100101100001110111110000111101011010011001100001')
    s = '0';e = 1023 - len(left_switch[0]);f = left_switch[2]
    # print(left_switch[0],len(left_switch[0]))   # 001 3
    e = bin(e)[2:]
    # print(e)      # 1111111100
    if len(e) < 11:
        e = '0' * (11-len(e)) + e
    # print(e)    # 11111111000
    Switch_number = double_precision.real_number([s,e,f])
    return Switch_number


def main():
    # f_r = bit_shift.main()
    # f_H,f_L,f_Lr,f_Hr,Bit_f = define(f_r[2])
    # print('f_H=\t %s\nf_L=\t%s%s\nf_Lr=\t %s'%(f_H,' '*27,f_L,f_Lr))
    # print('f_Hr=\t %s\nBit_f=\t %s'%(f_Hr,Bit_f))
    # B1_x = b1_x(5.1)
    # print('B1_x=\t ',B1_x)  # ('0', '10000000101', '0011001100101100001110111110000111101011010011001100')
    B2_x = b2_x(0.99)
    print(B2_x)             # ['0', '01111001011', '0000000000000000000000000000000000000000000000000000']
    # Real_number = double_precision.real_number(B2_x)
    # print(Real_number)


if __name__ == '__main__':
    main()