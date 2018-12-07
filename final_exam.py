def double_precision(number):
    if number > 0:
        s = '0'
    else:
        s = '1'
        number = -number
    power = 0
    while number > 2**power:
        power += 1
    exponent = 2 ** (power -1)
    e = bin((power - 1) + 1023)[2:]
    decimal = number - exponent
    f = ''
    while decimal > 0:
        if decimal*2.0 >= exponent:
            f = f + '1'
            decimal = decimal * 2.0 - exponent
        else:
            f = f + '0'
            decimal = decimal * 2.0
    # e不满11位左边补0
    if len(e) < 11:
        e = '0' * (11-len(e)) + e
    # f不满52位右边补0
    if len(f) < 52:
        f += '0' * (52-len(f))
    return s,e,f


def real_number(convert):
    s = convert[0]
    e = convert[1]
    f = convert[2]
    for i in range(1,len(f)+1):
        if f[-1] == '0':
           f = f[:-1]
        else:
            break
    for j in range(1,len(e)+1):
        if e[0] == '0':
            e = e[1:]
        else:
            break
    exponent = 2**(int(e,2)-1023)
    decimal = 0
    for k in range(1,len(f)+1):
        if f[-k] == '1':
            decimal = (decimal +exponent)/2
        else:
            decimal /= 2
    Real_number = exponent + decimal
    if s =='1':
        Real_number = -Real_number
    return Real_number


def left_bit_shift(f):
    cut = ''
    for i in range(len(f)):
        cut += f[i]
        if f[i] == '1':
            break
    remain = f[len(cut):]
    return cut,remain,remain+cut


def b2_x(number):
    double_pre = double_precision(number)
    Bit_f = define(double_pre[2])[4]
    left_switch = left_bit_shift(Bit_f)
    s = '0';e = 1023 - len(left_switch[0]);f = left_switch[2]
    e = bin(e)[2:]
    if len(e) < 11:
        e = '0' * (11-len(e)) + e
    Switch_number = real_number([s,e,f])
    return Switch_number


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
    f_H = f[:int(len(f)/2)]
    f_L = f[int(len(f)/2):]
    f_Lr = reverse(f_L)
    f_Hr = xor(f_H,f_Lr)
    Bit_f = f_Hr + f_L
    return f_H,f_L,f_Lr,f_Hr,Bit_f


def logistic_map(k,x):
    return 1 - k*x**2


def nested_iterations(x0,k,iterations):
    B2x = []
    for i in range(iterations):
        logi = logistic_map(k,x0)
        b2x = b2_x(logi)
        B2x.append(b2x)
        x0 = b2x
    return B2x


def main():
    x0 = 2.220446049250313e-16
    k = 2
    print(x0,k)
    nest = nested_iterations(x0,k,2)
    print(nest)


if __name__ == '__main__':
    main()