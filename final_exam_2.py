import numpy as np
import random, time
import math as mt
import matplotlib.pyplot as plt
import pandas as pd


def double_precision(number):
    """
    根据IEEE754标准，将给定的双精度实数转化为由三部分组成的二进制表示形式并返回
    :param                                     
        符号位     Sign         （s）      1 bit      
        指数部分   Exponent     （e）     11 bit
        尾数部分   Mantissa     （f）     52 bit
    :return: s,e,f
    """

    if number > 0:
        # 根据实数正负推出s的值
        s = '0'
    else:
        s = '1'
        # 若为负，则将实数取正
        number = -number

    # 若n>0, 2^n<number<2^(n+1) ==> number = 2^n * 1.f
    # 若n<0, 2^(n+1)<number<2^(n+2) ==> number = 2^n * 1.f
    power = 0
    # 当number>1,进入此循环，跳出循环后 n = power - 1 , 正好进入下一个while循环
    # 循环一次后即跳出，此时 n = power
    while number >= 2 ** power:
        power += 1
    # 当number<1,进入此循环，跳出循环后 n = power
    # 如果难以理解这个思想，试几组数据便能找到此规律
    while number < 2 ** power:
        power -= 1
    # 记录指数部分的值
    exponent = 2 ** power
    # 根据算出的2^n形式可推算出e的十进制数据
    # 将十进制数据转化为二进制之后的形式为0bxxxx
    # 有效数据为xxxx,截取出来赋值给e
    e = bin(power + 1023)[2:]
    # decimal 即为f的十进制形式
    decimal = number - exponent
    f = ''
    # 计算f的思路与十进制转二进制类似
    while decimal > 0:
        # 首先可以肯定的是decimal<exponent,因为目标f是二进制形式
        # 所以用倍乘2再与exponent比较
        # 如果大于等于，则上1，再decimal减去exponent
        # 如果小于，则上0
        # 如此迭代，直到decimal=0,循环结束
        # 最后，便能得到原始的二进制f形式
        if decimal * 2.0 >= exponent:
            f = f + '1'
            decimal = decimal * 2.0 - exponent
        else:
            f = f + '0'
            decimal = decimal * 2.0
    # 如果给出的实数本身为0,则按如下规定（bug1）
    if number == 0:
        s = '0';
        e = '0';
        f = '0'

    # 最后，进行e，f的填充，以符合规定的长度
    # e不满11位左边补0
    if len(e) < 11:
        e = '0' * (11 - len(e)) + e
    # f不满52位右边补0
    if len(f) < 52:
        f += '0' * (52 - len(f))
    return s, e, f


def real_number(convert):
    """
    即为double_precision函数的逆运算
    根据IEEE754标准，将给定的由三部分组成的二进制表示形式转化为双精度实数并返回
    """
    # 取出三个参数
    s, e, f = convert
    # 移除f的填充位
    for i in range(1, len(f) + 1):
        if f[-1] == '0':
            f = f[:-1]
        else:
            break
    # 移除e的填充位
    for j in range(1, len(e) + 1):
        if e[0] == '0':
            e = e[1:]
        else:
            break
    # 将移除填充位后的e转化为十进制计算出2^n,即exponent
    exponent = 2 ** (int(e, 2) - 1023)
    # 根据移除填充位后的f计算出f的十进制形式decimal
    decimal = 0
    # 简单的逆运算循环
    for k in range(1, len(f) + 1):
        if f[-k] == '1':
            decimal = (decimal + exponent) / 2
        else:
            decimal /= 2
    # 2^n + 0.f的十进制格式decimal <==> 2^n * 1.f
    Real_number = exponent + decimal
    # 根据s的值得出实数的正负，若为负，则添个负号
    if s == '1':
        Real_number = -Real_number
    return Real_number


def left_bit_shift(f):
    """
    {s,e,f}的第二类bit位变换中的f变换规则，左移位b操作
        b  : 移动的位数
    return ：移位部分，剩余部分，移位后的f
    """
    cut = ''
    # 从头遍历f，碰到'1'则停，遍历过的数字即为需要移位的部分
    for i in range(len(f)):
        cut += f[i]
        if f[i] == '1':
            break
    # f 中未遍历的部分
    remain = f[len(cut):]
    return cut, remain, remain + cut


def b2_x(number):
    """
    双精度实数的第二类bit位变换后，再返回相应的双精度实数
    """
    # 将双精度实数转化为符合IEEE754标准由三部分组成的二进制表示形式
    double_pre = double_precision(number)
    # 将转化后的参数之一 f 进行Bif{f}变换
    # 将Bif{f}变换后的Bit_f进行左移位b操作
    Bit_f = define(double_pre[2])[4]
    left_switch = left_bit_shift(Bit_f)
    # 将十进制参数e转化为二进制形式
    e = 1023 - len(left_switch[0])
    e = bin(e)[2:]

    # !!!如果e保持不变!!!
    # power = 0
    # while number >= 2 ** power:
    #     power += 1
    # while number < 2 ** power:
    #     power -= 1
    # e = bin(power + 1023)[2:]

    f = left_switch[2]
    # 根据相关定义进行赋值
    s = '0'
    # 对e进行右填充0操作
    if len(e) < 11:
        e = '0' * (11 - len(e)) + e
    # 根据参数s,e,f计算出对应的双精度函数
    Switch_number = real_number([s, e, f])

    # !!!如果s保持不变!!!
    # Switch_number = real_number([double_pre[0], e, f])

    return Switch_number


def b1_x(Real_number):
    double_pre = double_precision(Real_number)
    Bit_f = define(double_pre[2])[4]
    Switch_number = real_number([double_pre[0], double_pre[1], Bit_f])
    return Switch_number


def reverse(string):
    """字符串的逆序"""
    return string[::-1]


def xor(s1, s2):
    """二进制的异或操作"""
    result = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += '0'
        else:
            result += '1'
    return result


def define(f):
    """bit位变换的一些定义"""
    # 高位26bit
    f_H = f[:int(len(f) / 2)]
    # 低位26bit
    f_L = f[int(len(f) / 2):]
    # 低位26bit的倒置
    f_Lr = reverse(f_L)
    # 对应bit位异或运算的相关定义
    f_Hr = xor(f_H, f_Lr)
    # f的bit位变换
    Bit_f = f_Hr + f_L

    # ###########!!!TEST!!!#########
    # Bit_f = f_H + f_H
    # ###########!!!!!!!!!!#########

    return f_H, f_L, f_Lr, f_Hr, Bit_f


def logistic_map(k, x, iterations):
    result = []
    for i in range(iterations):
        x1 = 1 - k * x ** 2
        x = x1
        result.append(x)
    return result


def logistic2_map(k, x, iterations):
    result = []
    for i in range(iterations):
        x1 = k * x * (1 - x)
        x = x1
        result.append(x)
    return result


def save_data(origin, converted, filename):
    dirs = r'E:\JetBrains\data_file'
    filename = r'\%s.txt' % filename
    with open(dirs + filename, 'w') as f:
        for i in range(len(origin)):
            f.write(str(origin[i]) + '\t' + str(converted[i]))
            f.write('\n')


def draw(title, data, color, iterations, lab, para):
    hist, bin_edges = np.histogram(data, 1000)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value\n%s' % para)
    plt.ylabel('Frequency')
    plt.title('homogenize_%s' % title)
    plt.scatter([(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(len(hist))],
                hist / iterations, s=1, c=color, marker=',', label=lab)


def homogenize_logistic():
    x0 = 2 * random.random() - 1
    print(x0)
    k = 2
    iterations = 1000000
    logist = logistic_map(k, x0, iterations)
    homo = []
    for i in range(len(logist)):
        homo.append(b2_x(logist[i]))
        print(i, '\t', b2_x(logist[i]))
    title = 'logistic_data'
    save_data(logist, homo, title)
    para = 'system parameter k=%s, initial point x0 = %s' % (k, x0)
    draw(title, logist, 'b', iterations, 'Probability density before transformation', para)
    draw(title, homo, 'r', iterations, 'Probability density after transformation', para)
    plt.legend(loc='center')
    fig = plt.gcf()
    plt.show()
    fig.savefig(r'E:\JetBrains\file\%s_new.png' % title)

    # plt.hist(homo, 1000)
    # plt.show()


def homogenize_logistic2():
    x0 = random.random()
    print(x0)
    k = 4
    iterations = 1000000
    logist = logistic2_map(k, x0, iterations)
    homo = []
    for i in range(len(logist)):
        homo.append(b2_x(logist[i]))
        print(i, '\t', b2_x(logist[i]))
    title = 'logistic2_data'
    # save_data(logist, homo, title)
    para = 'system parameter k=%s, initial point x0 = %s' % (k, x0)
    draw(title, logist, 'b', iterations, 'Probability density before transformation', para)
    # draw(title,homo, 'r', iterations, 'Probability density after transformation', para)
    plt.legend(loc='center')
    fig = plt.gcf()
    plt.show()
    fig.savefig(r'E:\JetBrains\data_fig\%s_new.png' % title)


def Nested_iterations():
    x0 = random.random()
    k = 4
    x0 = logistic2_map(k, x0, 1000)[-1]
    nest = []
    iterations = 10000
    original = []
    for i in range(iterations):
        # 二类变换
        B2x = b2_x(x0)
        nest.append(B2x)
        x0 = logistic2_map(k, B2x, 1)[-1]
        original.append(x0)
        # 一类变换
        # B1x = b1_x(x0)
        # nest.append(B1x)
        # x0 = logistic2_map(k,B1x,1)[-1]

        print(i, '\t', B2x)
        # time.sleep(0.01)
    # plt.hist(nest, 1000)
    title = 'Nested_iterations_data'
    para = 'system parameter k=%s, initial point x0 = %s' % (k, x0)
    draw(title, original, 'b', iterations, 'Probability density before nested_iterations', para)
    # draw(title, nest, 'r', iterations, 'Probability density after nested_iterations', para)
    plt.legend(loc='upper center')
    fig = plt.gcf()
    plt.show()
    fig.savefig(r'E:\JetBrains\data_fig\%s_new.png' % title)


def PLM( x0):
    k = 4
    N = 64
    y = EOFError
    if x0 == 1:
        y = x0 - 1 / (100 * N)
    elif x0 % (1 / N) == 0:
        y = x0 + 1 / (100 * N)
    elif 0 < x0 < 1 / N:
        y = k * (N ** 2) * x0 * (1 / N - x0)

    else:
        for j in range(1, N):
            if j % 2 == 1 and j / N < x0 < (j + 1) / N:
                y = 1 - k * (N ** 2) * (x0 - j / N) * ((j + 1) / N - x0)
            elif j % 2 == 0 and j / N < x0 < (j + 1) / N:
                y = k * (N ** 2) * (x0 - j / N) * ((j + 1) / N - x0)
    return y


def PLM_homo():
    x0 = random.random()  # k=4;N=64
    x0_start = x0
    original = [];
    converted = [];
    length = 1000000
    for i in range(length):
        ori = PLM(x0)
        original.append(ori)
        con = b2_x(ori)
        converted.append(con)
        x0 = ori
        print(i, ori, con)

    title = 'PLM_homo'
    # print('data save start... ... ')
    # save_data(original, converted, title)
    # print('data save done!')
    para = 'system parameter k=%s, N  = %s, x0 = %s' % (4, 64, x0_start)
    draw(title, original, 'b', length, 'Probability density before transformation', para)
    draw(title, converted, 'r', length, 'Probability density after transformation', para)
    plt.legend(loc='upper center')
    fig = plt.gcf()
    plt.show()
    print('draw done!')
    fig.savefig(r'E:\JetBrains\data_fig\%s.png' % title)
    print('fig save done!')


def PLM_nested():
    x0 = random.random()  # k=4;N=64
    x0_start = x0
    original = [];
    converted = [];
    length = 100000
    for i in range(length):
        ori = PLM(x0)
        original.append(ori)
        con = b2_x(ori)
        converted.append(con)
        x0 = con
        print(i, ori, con)

    title = 'PLM_nested'
    print('data save start... ... ')
    save_data(original, converted, title)
    print('data save done!')
    para = 'system parameter k=%s, N  = %s, x0 = %s' % (4, 64, x0_start)
    draw(title, original, 'b', length, 'Probability density before transformation', para)
    draw(title, converted, 'r', length, 'Probability density after transformation', para)
    plt.legend(loc='upper center')
    fig = plt.gcf()
    plt.show()
    print('draw done!')
    fig.savefig(r'E:\JetBrains\data_fig\%s_new.png' % title)
    print('fig save done!')


def Two_Dimensional_Coupled_Map_Lattice():
    E = 0.2;
    R = 8;
    L = 8;
    iterations = 100000
    Lattice = []
    # Convert = np.zeros(iterations)
    Convert = []
    # print(Convert)
    for i in range(R):
        temp = []
        for j in range(L):
            temp.append(random.random())
        # print(temp)
        Lattice.append(temp)
    for k in range(iterations):
        for i in range(R):
            for j in range(L):
                self = Lattice[i][j]
                up = Lattice[(i - 1) % R][j]
                down = Lattice[(i + 1) % R][j]
                left = Lattice[i][(j - 1) % L]
                right = Lattice[i][(j + 1) % L]
                coupled = (1 - E) * PLM(self) + (E / 4) * (PLM(up) + PLM(down) + PLM(left) + PLM(right))
                # if coupled > 1:
                #     coupled = coupled - 1
                Lattice[i][j] = coupled
                # Convert[k]= coupled
                Convert.append(coupled)
                print(k, i, j, '\t', coupled)
    print(len(Convert))
    # plt.hist(Convert,1000)
    # plt.show()
    # homo = []
    # for i in range(len(Convert)):
    #     j = b2_x(Convert[i])
    #     homo.append(j)
    #     print(i,'\t',j)
    #
    # title = 'Two_dimensional_Coupled_Map_Lattice_Data'
    # # save_data(Convert,homo,title)
    # para = 'system parameter k=%s, N  = %s'%(4,64)
    # draw(title,Convert,'b',iterations*R*L,'Probability density before transformation',para)
    # draw(title,homo,'r',iterations*R*L,'Probability density after transformation',para)
    # plt.legend(loc = 'upper center')
    # fig = plt.gcf()
    # plt.show()
    # fig.savefig(r'E:\JetBrains\file\%s.png' % title)


def Two_Dimensional_Coupled_Map_Lattice_nested():
    E = 0.2
    R = 8
    L = 8
    iterations = 100000
    Lattice = []
    # Convert = np.zeros(iterations)
    Convert = []
    # print(Convert)
    for i in range(R):
        temp = []
        for j in range(L):
            temp.append(random.random())
        # print(temp)
        Lattice.append(temp)
    homo = []
    for k in range(iterations):
        for i in range(R):
            for j in range(L):
                self = Lattice[i][j]
                up = Lattice[(i - 1) % R][j]
                down = Lattice[(i + 1) % R][j]
                left = Lattice[i][(j - 1) % L]
                right = Lattice[i][(j + 1) % L]
                coupled = (1 - E) * PLM(self) + (E / 4) * (PLM(up) + PLM(down) + PLM(left) + PLM(right))
                # if coupled > 1:
                #     coupled = coupled - 1

                Convert.append(coupled)
                nest = b2_x(coupled)
                homo.append(nest)
                Lattice[i][j] = nest
                print(k, i, j, '\t', coupled, '\t', nest)
    print(len(Convert))
    # plt.hist(Convert,1000)
    # plt.show()

    # for i in range(len(Convert)):
    #     j = b2_x(Convert[i])
    #     homo.append(j)
    #     print(i,'\t',j)

    title = 'Two_dimensional_Coupled_Map_Lattice_Data'
    print('data save start... ... ')
    save_data(Convert, homo, title)
    print('data save done!')
    para = 'system parameter k=%s, N  = %s' % (4, 64)
    draw(title, Convert, 'b', iterations * R * L, 'Probability density before transformation', para)
    draw(title, homo, 'r', iterations * R * L, 'Probability density after transformation', para)
    plt.legend(loc='upper center')
    fig = plt.gcf()
    plt.show()
    print('draw done!')
    fig.savefig(r'E:\JetBrains\data_fig\%s_new.png' % title)
    print('fig save done!')


def new_cubic(x):
    a = 4;
    N = 64
    i = ((x + 1) * N) / 2
    if i != int(i):
        i = mt.ceil((((x + 1) * N) / 2))
    else:
        i = int(i + 1)
    x1 = a * (N * x + N + 1 - 2 * i) ** 3 + (1 - a) * (N * x + N + 1 - 2 * i)
    x = x1
    return x


def new_cubic_b2x():
    x0 = 0.123456789
    nest = []
    iterations = 100000
    original = []
    for i in range(iterations):
        # 二类变换
        B2x = b2_x(x0)
        nest.append(B2x)
        x0 = new_cubic(B2x)
        original.append(x0)
        # 一类变换
        # B1x = b1_x(x0)
        # nest.append(B1x)
        # x0 = logistic2_map(k,B1x,1)[-1]

        print(i, '\t', B2x)
        # time.sleep(0.01)
    # plt.hist(nest, 1000)
    title = 'new_cubic_data'
    para = 'system parameter a=4, N = 64'
    draw(title, original, 'b', iterations, 'Probability density before', para)
    draw(title, nest, 'r', iterations, 'Probability density after', para)
    plt.legend(loc='upper center')
    # fig = plt.gcf()
    plt.show()
    # fig.savefig(r'E:\JetBrains\data_fig\%s_new.png' % title)


def main():
    # PLM(0.251)
    # homogenize_logistic2()
    # homogenize_logistic()
    # Nested_iterations()
    # Two_Dimensional_Coupled_Map_Lattice()
    # Two_Dimensional_Coupled_Map_Lattice_nested()
    # PLM_nested()
    # PLM_homo()

    # b2_x map
    # x = [];y=[]
    # for i in np.arange(-1,1,0.0001):
    #     x.append(i)
    #     map = b2_x(i)
    #     y.append(map)
    #     print(i,'\t',map)
    #     # plt.scatter(i,map, s=10, c='b', marker='o')
    # plt.plot(x, y, marker='.', linestyle='' '')
    # plt.xlabel('x_n')
    # plt.ylabel('x_(n+1)')
    # plt.title('The b2_x  map when x in (-1, 1, 0.0001)')
    # plt.show()

    # b2_(logistic2_x) map
    # x = [];y = []
    # for i in np.arange(-1, 1, 0.0001):
    #     x.append(i)
    #     logi2 = logistic2_map(4,i,1)[-1]
    #     map = b2_x(logi2)
    #     y.append(map)
    #     print(i, '\t',logi2,'\t', map)
    #     # plt.scatter(i,map, s=10, c='b', marker='o')
    # plt.plot(x, y, marker='.', linestyle='' '')
    # plt.xlabel('x_n')
    # plt.ylabel('x_(n+1)')
    # plt.title('The b2_(logistic2_x)  map when x in (-1, 1, 0.0001)')
    # plt.show()

    # 数据测试,统计大小大小对数(以0.5为界限)
    # x0 = 0.1;x=[];num=[];count = 0;length = 10000
    # for i in range(length):
    #     x.append(i)
    #     logi = logistic2_map(4,x0,1)[-1]
    #     x1 = b2_x(logi)
    #     if i!=0 and (x1>0.5>x0 or x1<0.5<x0):
    #         count += 1
    #     x0 = x1
    #     num.append(x0)
    #     print(i,x0)
    # print('\n\n',count,'\n',count/(length-1))
    #
    # plt.plot(x,num,marker = '.',linestyle = '-')
    # plt.show()

    new_cubic_b2x()


if __name__ == '__main__':
    main()
