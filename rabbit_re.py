WORDSIZE = 2 ** 32


def str2int(string):
    return int(string, 16)


def int2str(hexadecimal):
    return hex(hexadecimal)[2:].upper()


def left_rotation(v, n):
    bi = bin_str(v).replace(' ', '')
    lr = bi[n:] + bi[:n]
    return int(lr, 2)


def bin_str(x):
    bin = ''
    while x > 0:
        if len(bin) != 0 and len(bin.replace(' ', '')) % 4 == 0:
            bin = ' ' + bin
        bin = str(x % 2) + bin
        x = int(x / 2)
    while len(bin.replace(' ', '')) < 32:
        if len(bin.replace(' ', '')) % 4 == 0:
            bin = ' ' + bin
        bin = '0' + bin
    return bin


def print_IS(state):
    for i in range(8):
        print("IS.X[%d]=%X" % (i, state.X[i]))
        print("IS.C[%d]=%X" % (i, state.C[i]))
    print("IS.b=%X" % state.b)
    print('\n')


class InnerState:
    def __init__(self, key):
        key = key.replace(' ', '')
        K = []
        self.X = []
        self.C = []
        for i in range(8):
            temp = key[(7 - i) * 4:(8 - i) * 4]
            K.append(temp)
        for j in range(8):
            if j % 2 == 0:
                x = K[(j + 1) % 8] + K[j]
                c = K[(j + 4) % 8] + K[(j + 5) % 8]
                self.X.append(str2int(x))
                self.C.append(str2int(c))
            else:
                x = K[(j + 5) % 8] + K[(j + 4) % 8]
                c = K[j] + K[(j + 1) % 8]
                self.X.append(str2int(x))
                self.C.append(str2int(c))
        self.b = 0


def g_function(u, v):
    x = u + v
    l = x * x
    m = l >> 32
    g = l ^ m
    return g % (2 ** 32)


def next_state(state):
    A = ['4D34D34D', 'D34D34D3', '34D34D34', '4D34D34D',
         'D34D34D3', '34D34D34', '4D34D34D', 'D34D34D3']
    for m in range(8):
        temp = state.C[m] + str2int(A[m]) + state.b
        state.b = int(temp / WORDSIZE)
        state.C[m] = temp % WORDSIZE
    G = []
    for k in range(8):
        g = g_function(state.X[k], state.C[k])
        G.append(g)
    for n in range(8):
        if n % 2 == 0:
            temp = (G[n] + left_rotation(G[(n - 1) % 8], 16) + left_rotation(G[(n - 2) % 8], 16)) % WORDSIZE
        else:
            temp = (G[n] + left_rotation(G[(n - 1) % 8], 8) + G[(n - 2) % 8]) % WORDSIZE
        state.X[n] = temp


def key_setup(master):
    # for i in range(4):
    #     next_state(master)
    for j in range(8):
        master.C[j] ^= master.X[(j + 4) % 8]


def initialization_vector(iv, state):
    iv = iv.replace(' ', '')
    IV = []
    for i in range(4):
        temp = iv[(3 - i) * 4:(4 - i) * 4]
        IV.append(temp)
    concatenation = [IV[1] + IV[0], IV[3] + IV[1], IV[3] + IV[2], IV[2] + IV[0]]
    wk = state
    for j in range(8):
        wk.C[j] = state.C[j] ^ str2int(concatenation[j % 4])
    for i in range(4):
        next_state(state)
    return wk


def extraction_scheme(wk):
    def split(x):
        string = int2str(x)
        if len(string) < 4:
            string = '0' * (4 - len(string)) + string
        head = string[:int(len(string) / 2)]
        end = string[int(len(string) / 2):]
        return [str2int(head), str2int(end)]

    S = []
    for i in range(8):
        if i % 2 == 0:
            s = int2str(split(wk.X[i])[0] ^ split(wk.X[(i + 5) % 8])[1])
        else:
            s = int2str(split(wk.X[i - 1])[1] ^ split(wk.X[(i + 2) % 8])[0])
        if len(s) < 4:
            s = '0' * (4 - len(s)) + s
        S.append(s)
    return " ".join(str(i) for i in S)


def en_decryption(wk):
    pass


if __name__ == '__main__':
    key = '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
    mt = InnerState(key)
    key_setup(mt)
    for j in range(8):
        next_state(mt)
        mt.C[j] ^= mt.X[(j + 4) % 8]
        for i in range(10):
            S = extraction_scheme(mt)
            print("S[%d][%d] = " % (j, i), S)
            next_state(mt)
