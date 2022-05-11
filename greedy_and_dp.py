from random import randint

m = 5
p = sorted([randint(10, 500) for x in range(30)])
n = len(p)


def dp(n, m, p):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == j:
                dp[i][j] = dp[i][j - 1] + p[j]
            elif i > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1] + (dp[i][j - i - 1] -
                                           dp[i][j - i - 2]) + p[j]
    return dp[-1][-1]


def greedy(n, m, p):
    ans = 0
    machines = [[0] for _ in range(m)]
    for w, i in zip(p, range(n)):
        machines[i % m].append(w + machines[i % m][-1])
        ans += machines[i % m][-1]
    m = [0]
    return ans


for i in range(400):
    m=randint(1, 1000)
    p = sorted([randint(10, 500) for x in range(30)])
    n = len(p)
    a = greedy(n, m, p)
    b = dp(n, m, p)
    # print(a,b)
    if a != b:
        print('false',a, b)
