# 求向量的特征值，特征向量
# import numpy as np
# A = [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
# # print('打印A：\n{}'.format(A))
# a，b= np.linalg.eig(A)
# # print('打印特征值a：\n{}'.format(a))
# # print('打印特征向量b：\n{}'.format(b))

# 求向量模长(一范二范)
# import numpy as np
# x = np.array([3,4])
# print(np.linalg.norm(x))    # 5
# #  默认为2范数,下面是一范数
# print(np.linalg.norm(x,ord=1))# 7
# x = np.array([3])
# print(np.linalg.norm(x,ord=2))    # 5
#  默认为2范数,下面是一范数
# print(np.linalg.norm(x,ord=1))# 7

# 求向量的内积和对应元素相乘
# import numpy as np
# 2-D array: 2 x 3
# two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# 2-D array: 3 x 2
# two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])
# two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
# print('two_multi_res:\n %s' %(two_multi_res))
# 1-D array
# one_dim_vec_one = np.array([1, 2, 3])
# one_dim_vec_two = np.array([4, 5, 6])
# one_result_res = np.dot(one_dim_vec_one, one_dim_vec_two)
# print('one_result_res:\n %s' %(one_result_res))
# 2-D array: 2 x 3
# two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# another_two_dim_matrix_one = np.array([[7, 8, 9], [4, 7, 1]])
# # 对应元素相乘 element-wise product
# element_wise = two_dim_matrix_one * another_two_dim_matrix_one
# print('element wise product:\n %s' %(element_wise))
#
# # 对应元素相乘 element-wise product
# element_wise_2 = np.multiply(two_dim_matrix_one, another_two_dim_matrix_one)
# print('element wise product:\n %s' % (element_wise_2))




