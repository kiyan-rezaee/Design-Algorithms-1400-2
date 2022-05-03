import time
from random import randint


# version 1
def knapsack1(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


# version 2
def knapsack2(W, wt, val, n):
    Kp = [0 for i in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                Kp[w] = max(Kp[w], Kp[w - wt[i - 1]] + val[i - 1])
            else:
                break
    return Kp[W]

val = [randint(10, 500) for x in range(1000)]
wt = [randint(10, 500) for x in range(1000)]

W = 4000
n = len(val)

t = time.time()
print(knapsack1(W, wt, val, n))
print('knapsack1 runtime:',-(t - time.time()))
t = time.time()
print(knapsack2(W, wt, val, n))
print('knapsack2 runtime:',-(t - time.time()))
