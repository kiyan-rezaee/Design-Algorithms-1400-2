import time
from random import randint


def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]  # Making the dp array

    for i in range(1, n+1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i-1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
            else:  # idea talai mehrshad
                break
    return dp[W]  # returning the maximum value of knapsack

def knapSack2(W, wt, val, n):
    dp = [0 for i in range(W+1)]  # Making the dp array

    for i in range(1, n+1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i-1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
            else:  # idea talai mehrshad
                break
    return dp[W]  # returning the maximum value of knapsack

val = [randint(10, 500) for x in range(1000)]
wt = [randint(10, 500) for x in range(1000)]

W = 4000
n = len(val)

t = time.time()
print(knapSack(W, wt, val, n))
print(-(t-time.time()))
t = time.time()
k = sorted([(x, y) for x, y in zip(val, wt)], key=lambda x: x[1])
val = [x[0] for x in k]
wt = [x[1] for x in k]
print(knapSack2(W, wt, val, n))
print(-(t-time.time()))
