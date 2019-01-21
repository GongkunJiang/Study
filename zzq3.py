data = """f0 6a c9 c0 c1 69 a1 68 70 24 4d 88 62 81 e5 c6
8f 11 d4 04 eb 46 f1 86 ea 45 03 e4 65 07 51 96
c4 58 0c 59 e0 44 8d 06 36 a4 56 66 b6 ce 5d a0
54 d8 3b 1e b1 6e 50 9d 60 67 6c dc 34 2d bd 7a
f4 c7 8b 92 b9 48 21 7d 0a 90 8c af 80 2b b2 fd
75 2c d0 e2 a2 6b ee 2a 9a c3 41 13 db 37 a9 fc
a7 09 a3 42 3e 39 cd e6 e7 a6 94 78 38 4b f8 b0
3f 10 1f a5 f9 bb f5 20 99 a8 df 16 9e be 76 6f
ff cb f3 8e 5c c2 79 b4 d3 14 49 4c 52 dd 47 01
d2 02 00 30 aa 6d c8 e8 d9 4f 1c 5a d6 27 7b 1a
32 b3 31 4a 18 9b 0e 19 e1 17 b7 d7 f2 77 2f de
85 73 64 23 3a 74 ef e3 5e 12 05 ed 3d b5 ae 7e
fb e9 bc d5 0d 33 da 1d 95 57 89 35 15 9c 0f 91
fe 29 82 8a ad 87 ec 9f ab 22 5b d1 cc 3c b8 71
93 28 43 f6 ac 1b 63 53 0b 97 98 55 fa ba 08 25
83 72 2e bf ca 26 7c 4e c5 84 61 40 cf 5f 7f f7"""

s = data.replace("\n", " ").split(" ")
print(s)
i = 1
for d in s:
    d = '0' * (3 - len(str(int(d, 16)))) + str(int(d, 16))
    if i % 16 != 0:
        print(d + "\t", end="")
    else:
        print(d)
    i += 1
