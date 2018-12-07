import double_precision


def left_bit_shift(f):
    cut = ''
    for i in range(len(f)):
        cut += f[i]
        if f[i] == '1':
            break
    remain = f[len(cut):]
    return cut,remain,remain+cut


def right_bit_shift(f,b):
    cut = '0' *(b-1) + '1'
    remain = f[:len(f)-b]
    return cut, remain, cut + remain


def main():
    convert = double_precision.double_precision(0.5)
    f_l = left_bit_shift(convert[2])
    print('cut=\t',f_l[0],'\nremain= ',f_l[1])
    print('f(<-%s)= %s' %(len(f_l[0]),f_l[2]))
    # b = 20
    # f_r = right_bit_shift(f_l[2],b)
    # print('remain= ', f_r[1],'\ncut=\t', f_r[0])
    # print('f(->%s)= %s' % (b, f_r[2]))
    return f_l


if __name__ == '__main__':
    main()