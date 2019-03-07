# My name is Ran Liao
# My extension id is X154149

import numpy as np
import matplotlib.pyplot as plt
import math


def sma(A, width=2):
    result = []
    for i in range(A.shape[0] - width + 1):
        sum = 0
        for j in range(width):
            sum += A[i + j]
        sum /= width
        result.append(sum)
    return np.array(result)


# cumulative moving average
def cma(A):
    result = []
    sum = 0
    for i in range(A.shape[0]):
        sum += A[i]
        result.append(sum / (i + 1))
    return np.array(result)


if __name__ == "__main__":
    A = []
    for i in range(12):
        A.append(5 + 2 * i)
    A = np.array(A)
    print('The original data:', A)

    B = sma(A)
    B_width = A.shape[0] - B.shape[0] + 1
    B_CMA = cma(B)
    print('Current window width:', B_width)
    print('The SMA result is', B)
    print('The CMA of this SMA is', B_CMA)

    C = sma(A, 4)
    C_width = A.shape[0] - C.shape[0] + 1
    C_CMA = cma(C)
    print('Current window width:', C_width)
    print('The SMA result is', C)
    print('The CMA of this SMA is', C_CMA)

    # plot
    x = B
    y = np.sin(B * math.pi / 2)
    plt.plot(x, y, marker="*", linewidth=3,
             linestyle="--", color="orange",
             label="B")
    x = C
    y = np.sin(C * math.pi / 2)
    plt.plot(x, y, marker="+", linewidth=1,
             linestyle="-", color="blue",
             label="C")
    plt.title("sin(B * PI / 2) AND sin(C * PI / 2)")
    plt.grid(True)
    plt.legend(["B", "C"])
    plt.show()
