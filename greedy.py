def greedy(n,m,p):
    ans = 0
    machines = [[0] for _ in range(m)]
    for w,i in zip(p,range(n)):
        machines[i%m].append(w+machines[i%m][-1])
        ans+=machines[i%m][-1]

    return ans, machines

n=7
m=2
p=[2,6,13,17,21,24,26]
print(greedy(n,m,p))
# ans=0
# dp=[[0 for _ in range(n+1)] for _ in range(m)]
# print(dp)
# for i in range(m):
#     for j in range(1,n+1):
#         if i==0:
#             dp[i][j] = dp[i][j-1]+sum(p[:j])
#         else:
#             dp[i][j] = dp[i-1][j]
#             s = 1
#             print(i,j)
#             for k in range(j-i,max(j-i-i,-1),-1):
#                 print(k)
#                 s = -s
#                 # print(i,k,dp[i][k])
#                 dp[i][j] += dp[i][k]*s
# print(dp)
# #[[0,2,10,31,69,128]1
# # [0,2,8, 23,46,82]2 8=> 10-2/23=>31-8/46=>69-23/82=>128-46 (ok)
# # [0,2,8,21,40,67]3 21=> 23-2+0/40=> 46-8+2/67=>82-21+8-2
# # [0,2,8,21,38,61]4 38=> 40-2+0/61=>67-8+2
# # [0,2,8,21,38,59]]5 59=> 61-2
#(211, [[0, 2, 8, 21, 38, 59, 83]])
