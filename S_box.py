def str2int(string):
    return int(string, 16)


def int2str(hexadecimal):
    temp = hex(hexadecimal)[2:].upper()
    if len(temp) < 2:
        temp = '0' + temp
    return temp


def initialization():
    S_box = []
    for i in range(16):
        s = []
        for j in range(16):
            s.append(int2str(i * 16 + j))
        S_box.append(s)
    return S_box


def print_box(box):
    for i in range(16):
        print("\t%X" % i, end='')
        if i == 15:
            print()
    for j in range(16):
        print("%X" % j, end='')
        for k in range(16):
            print("\t%s" % box[j][k], end='')
            if k == 15:
                print()


def dec2bin(num):
    return bin(num)[2:]


def bin2dec(string):
    return int(string, 2)


def polynomial_multiply(x, y):
    bin_x, bin_y, xor = dec2bin(x), dec2bin(y), 0
    for power in range(len(bin_y)):
        carry = int(bin_y[-1 - power])
        if carry == 1:
            temp = x << power
            xor ^= temp
    return xor


def polynomial_divide(x, y):
    bin_x, bin_y, quotient, remainder, bin_remainder = dec2bin(x), dec2bin(y), 0, x, dec2bin(x)
    while remainder >= y:
        quotient += 1 << (len(bin_remainder) - len(bin_y))
        temp = y << (len(bin_remainder) - len(bin_y))
        remainder ^= temp
        bin_remainder = dec2bin(remainder)
    return quotient, remainder


def polynomial_inverse(x, y):
    if y == 0:
        return 0
    v, w, q, r = [0, 1], [1], [0], [y]
    r.append(polynomial_divide(x, y)[1])
    q.append(polynomial_divide(x, y)[0])
    w.append(q[1])
    while r[-1] != 0:
        q.append(polynomial_divide(r[-2], r[-1])[0])
        v.append(v[-2] ^ (polynomial_multiply(q[-1], v[-1])))
        w.append(w[-2] ^ (polynomial_multiply(q[-1], w[-1])))
        r.append(polynomial_divide(r[-2], r[-1])[1])
    return w[-2]


def box_inverse(box):
    a = 0b100011011
    inverse = box
    for i in range(16):
        for j in range(16):
            inverse[i][j] = int2str(polynomial_inverse(a, str2int(box[i][j])))
    return inverse


def bit_shift(string):
    num = str2int(string)
    num_bin = dec2bin(num)[::-1]
    if len(num_bin) < 8:
        num_bin += '0' * (8 - len(num_bin))
    shift = []
    c = '01100011'[::-1]
    for i in range(len(num_bin)):
        shift.append(str(int(num_bin[i]) ^ int(num_bin[(i + 4) % 8]) ^ int(num_bin[(i + 5) % 8]) ^ int(
            num_bin[(i + 6) % 8]) ^ int(num_bin[(i + 7) % 8]) ^ int(c[i])))
    return int2str(bin2dec(''.join(shift)[::-1]))


def box_shift(box):
    shift = box
    for i in range(16):
        for j in range(16):
            shift[i][j] = bit_shift(box[i][j])
    return shift


def inverse_shift(string):
    num = str2int(string)
    num_bin = dec2bin(num)[::-1]
    if len(num_bin) < 8:
        num_bin += '0' * (8 - len(num_bin))
    shift = []
    d = '00000101'[::-1]
    for i in range(len(num_bin)):
        shift.append(str(int(num_bin[(i + 2) % 8]) ^ int(num_bin[(i + 5) % 8]) ^ int(num_bin[(i + 7) % 8]) ^ int(d[i])))
    return int2str(bin2dec(''.join(shift)[::-1]))


def box_inverse_shift(box):
    shift = box
    for i in range(16):
        for j in range(16):
            shift[i][j] = inverse_shift(box[i][j])
    return shift


if __name__ == '__main__':
    s_box = box_shift(box_inverse(initialization()))
    print_box(s_box)
    inverse_s_box = box_inverse(box_inverse_shift(initialization()))
    print('#' * 80)
    print_box(inverse_s_box)