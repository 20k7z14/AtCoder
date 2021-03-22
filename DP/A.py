import sys
import os
f = open('test.txt','r')
sys.stdin = f

def chmin(dp,i,b):
    if dp[i] > b:
        dp[i] = b
        return True
    else:
        return False

inf = 10**5
N = int(input())
h = list(map(int,input().split()))
dp = [inf]*N

dp[0] = 0
for i in range(1,N):
    chmin(dp,i,dp[i-1]+abs(h[i]-h[i-1]))
    if i>1:
        chmin(dp,i,dp[i-2]+abs(h[i]-h[i-2]))

print(dp[-1])
