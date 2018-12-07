from final_exam_2 import *
path = r'C:\Users\Administrator.YLMF-20150729SV\Documents\Tencent Files\1193417901\FileRecv'
filename = r'test2.txt'
homo = []
for line in open(path+'\\'+filename,'r'):
    h = b2_x(float(line))
    # print(line,h)
    homo.append(h)

# draw('lz_homo',homo,'b',3000,'Probability density after transformation', 'pass')
with open(path+'\\homo_text2.txt','w') as f:
    for i in range(len(homo)):
        f.write(str(homo[i]))
        f.write('\n')