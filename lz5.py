import time

# 测试表明写文件先把数据存为字符串最佳
path = r"C:\Users\Administrator.YLMF-20150729SV\Documents\Tencent Files\1193417901\FileRecv"

file = path + "\\" + "bittest8.txt"
file2 = path + "\\" + "bittest8done.txt"

data = []

start = time.clock()
for line in open(file):
    s = line[-9:]
    # print(s)
    data.append(s)
with open(file2, 'w') as f:
    for i in range(len(data)):
        f.write(data[i])
end = time.clock()
print(end - start)  # 0.17806593871388096

data = ""

start = time.clock()
for line in open(file):
    s = line[-9:]
    # print(s)
    data += s
with open(file2, 'w') as f:
    f.write(data)
end = time.clock()
print(end - start)  # 0.11631145017276182

start = time.clock()
for line in open(file):
    s = line[-9:]
    # print(s)
    with open(file2, 'w') as f:
        f.write(s)
end = time.clock()
print(end - start)  # 92.14758553341565
