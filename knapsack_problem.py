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
    dp = [0 for i in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
            else:
                break
    return dp[W]


val = [randint(10, 500) for x in range(1000)]
wt = [randint(10, 500) for x in range(1000)]

W = 4000
n = len(val)

# k = sorted([(x, y) for x, y in zip(val, wt)], key=lambda x: x[1])
# val = [x[0] for x in k]
# wt = [x[1] for x in k]

t = time.time()
print(knapsack(W, wt, val, n))
print(-(t - time.time()))
