import random, time


def PLM1(k, N, x):
    y = EOFError
    if x == 1:
        y = x - 1 / (100 * N)
    elif x % (1 / N) == 0:
        y = x + 1 / (100 * N)
    elif 0 < x < 1 / N:
        y = k * (N ** 2) * x * (1 / N - x)

    else:
        for j in range(1, N):
            if j % 2 == 1 and j / N < x < (j + 1) / N:
                y = 1 - k * (N ** 2) * (x - j / N) * ((j + 1) / N - x)
            elif j % 2 == 0 and j / N < x < (j + 1) / N:
                y = k * (N ** 2) * (x - j / N) * ((j + 1) / N - x)
    return y


def PLM2(k, N, x):
    y = EOFError
    if x == 1:
        y = x - 1 / (100 * N)
    elif x % (1 / N) == 0:
        y = x + 1 / (100 * N)
    elif 0 < x < 1 / N:
        y = k * (N ** 2) * x * (1 / N - x)

    else:
        j = int(x * N)  # 直接判断x落在区间的第几段
        if j % 2 == 1 and j / N < x < (j + 1) / N:
            y = 1 - k * (N ** 2) * (x - j / N) * ((j + 1) / N - x)
        elif j % 2 == 0 and j / N < x < (j + 1) / N:
            y = k * (N ** 2) * (x - j / N) * ((j + 1) / N - x)
    return y


if __name__ == '__main__':
    k, N, x = 4, 10000000, random.random()
    time_start = time.clock()
    plm1 = PLM1(k, N, x)
    time_end = time.clock()
    time_consuming1 = time_end - time_start
    print(time_consuming1)  # 2.903729164198108

    time_start = time.clock()
    plm2 = PLM2(k, N, x)
    time_end = time.clock()
    time_consuming2 = time_end - time_start
    print(time_consuming2)  # 1.1817981930395405e-05
