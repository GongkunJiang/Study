import homogenize_logistic,bit_switch


original_data = homogenize_logistic.logistic_map(4,0.3345,50)
print(original_data)
dirs = r'E:\JetBrains\file'
filename = r'\logistic4.txt'
with open(dirs+filename,'w') as f:
    for i in range(len(original_data)):
        f.write(str(original_data[i])+'\t\t\t'+str(bit_switch.b2_x(original_data[i])))
        f.write('\n')