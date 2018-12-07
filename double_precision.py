def double_precision(real_number):
    if real_number[0] > 0:
        s = '0'
    else:
        s = '1'
        real_number = -real_number
    power = 0
    while real_number > 2**power:
        power += 1
    exponent = 2 ** (power -1)
    e = bin((power - 1) + 1023)[2:]
    decimal = real_number - exponent
    f = ''
    while decimal > 0:
        if decimal*2.0 >= exponent:
            f = f + '1'
            decimal = decimal * 2.0 - exponent
        else:
            f = f + '0'
            decimal = decimal * 2.0
    # print(e)
    # e不满11位左边补0
    if len(e) < 11:
        e = '0' * (11-len(e)) + e
    # f不满52位右边补0
    if len(f) < 52:
        f += '0' * (52-len(f))
    return s,e,f


def real_number(convert):
    # print(convert)
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


def main():
    # Real_number = 0.5
    # # convert = input('Please input a real number:\n')
    # convert = double_precision(Real_number)
    # # ('0', '10000000101', '0000000000000001010000111010000111101011010011001100')
    # print('Convert result:%s\n\t=\t %s'%(Real_number,convert))
    # print('s=\t\t', convert[0], '\ne=\t\t', convert[1], '\nf=\t\t', convert[2])
    # # Rn = real_number(convert)
    # # print(Rn)
    # return convert
    pass


if __name__ == '__main__':
    main()