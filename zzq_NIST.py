import numpy as np
import random, time
import math as mt
import matplotlib.pyplot as plt
import pandas as pd


a = 4
N = 128


def init_newcubic(x, n):
    for q in range(n):
        i = ((x + 1) * N) / 2
        if i == int(i) and i != N:  # x=-1,2-N/N,4-N/N,…………的情况，让它落到下一段去
            i = i + 1
            x = x + (1 / 100 * N)
        elif i == N:  # x=1的情况，落到当前端即最后一段
            i = N
            x = x - (1 / 100 * N)
        elif i == mt.ceil(i) - 0.5:
            i = mt.ceil(i)
            x = x + (1 / 100 * N)
        elif i == mt.ceil(i) - 0.25 or i == mt.ceil(i) - 0.75:
            i = mt.ceil(i)
            x = x + (1 / 100 * N)
        else:
            i = mt.ceil(i)  # ceil函数为取上整
        x1 = a * (N * x + N - 2 * i + 1) ** 3 + (1 - a) * (N * x + N - 2 * i + 1)
        x = x1
    return x


def PRNG(x, n):
    keystrlist = []
    for q in range(n):
        print(q)
        i = ((x + 1) * N) / 2
        if i == int(i) and i != N:  # x=-1,2-N/N,4-N/N,…………的情况，让它落到下一段去
            i = i + 1
            x = x + (1 / 100 * N)
        elif i == N:  # x=1的情况，落到当前端即最后一段
            i = N
            x = x - (1 / 100 * N)
        elif i == mt.ceil(i) - 0.5:
            i = mt.ceil(i)
            x = x + (1 / 100 * N)
        elif i == mt.ceil(i) - 0.25 or i == mt.ceil(i) - 0.75:
            i = mt.ceil(i)
            x = x + (1 / 100 * N)
        else:
            i = mt.ceil(i)  # ceil函数为取上整

        x1 = a * (N * x + N - 2 * i + 1) ** 3 + (1 - a) * (N * x + N - 2 * i + 1)

        if x1 >= 0:
            t1 = x1
        if x1 < 0:
            t1 = x1 + 1

        keystr = getkeystr(t1)
        # print(keystr)
        keystrlist.extend(keystr)
        # print(keystrlist)
        if q % 5000000 == 0 and q != 0:
            write_file(keystrlist)
            keystrlist = []
        elif q == 31499999:
            write_file(keystrlist)
            print('OK')
        x = x1


def getkeystr(x):
    temp1 = int(x * (2 ** 12))
    a1 = int(((x * (2 ** 12)) - temp1) * (2 ** 4))
    temp2 = int(x * (2 ** 16))
    a2 = int(((x * (2 ** 16)) - temp2) * (2 ** 4))
    temp3 = int(x * (2 ** 20))
    a3 = int(((x * (2 ** 20)) - temp3) * (2 ** 4))
    temp4 = int(x * (2 ** 24))
    a4 = int(((x * (2 ** 24)) - temp4) * (2 ** 4))
    temp5 = int(x * (2 ** 28))
    a5 = int(((x * (2 ** 28)) - temp5) * (2 ** 4))
    temp6 = int(x * (2 ** 32))
    a6 = int(((x * (2 ** 32)) - temp6) * (2 ** 4))
    temp7 = int(x * (2 ** 36))
    a7 = int(((x * (2 ** 36)) - temp7) * (2 ** 4))
    temp8 = int(x * (2 ** 40))
    a8 = int(((x * (2 ** 40)) - temp8) * (2 ** 4))

    k1 = F(a1, a3, a2)
    k2 = F(a2, a4, a3)
    k3 = F(a3, a5, a4)
    k4 = F(a4, a6, a5)
    k5 = F(a5, a7, a6)
    k6 = F(a6, a8, a7)
    k7 = F(a7, a1, a8)
    k8 = F(a8, a2, a1)
    k = ((((((k1 * 16 + k2) * 16 + k3) * 16 + k4) * 16 + k5) * 16 + k6) * 16 + k7) * 16 + k8
    keystr = bin(k)[2:].rjust(32, '0')
    return keystr


def F(a, b, c):
    k = ((a + b) % 16) ^ c
    return k

def write_file(keystrlist):
    fh = open('newcubic32.txt', 'a')
    fh.writelines(keystrlist)
    fh.flush()
    fh.close()


if __name__ == '__main__':
    x0 = 0.456789123
    x0 = init_newcubic(x0, 1000)
    PRNG(x0, 31500000)

