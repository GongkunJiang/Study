from final_exam_2 import *
import matplotlib.pyplot as plt
E = 1


def founction(x):
    # x1 = EOFError
    # if -1 <= x < -0.5:
    #     x1 = E * (256 * x ** 3 + 576 * x ** 2 + 420 * x + 99)
    # elif -0.5 <= x < 0:
    #     x1 = E * (256 * x ** 3 + 192 * x ** 2 + 36 * x + 1)
    # elif 0 <= x < 0.5:
    #     x1 = E * (256 * x ** 3 - 192 * x ** 2 + 36 * x - 1)
    # elif 0.5 <= x <= 1:
    #     x1 = E * (256 * x ** 3 - 576 * x ** 2 + 420 * x - 99)
    x1 = 4*x**3 - 3*x**2
    return x1


if __name__ == '__main__':
    x0 = 0.123456789

    nest = []
    iterations = 1000000
    for i in range(iterations):
        Fun = founction(x0)
        # Fun = logistic2_map(4,x0,1)[-1 ]
        B2x = b2_x(Fun)
        nest.append(B2x)
        x0 = B2x
        # print(i, '\t', Fun,'\t',B2x)
        print(i)
    title = 'Founction Nested'
    para = 'system parameter E=%s' % E
    draw(title, nest, 'r', iterations, 'Probability density after nested_iterations', para)
    plt.legend(loc='upper center')
    fig = plt.gcf()
    plt.show()