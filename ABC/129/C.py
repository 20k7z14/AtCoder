import sys
import os
f = open('test.txt','r')
sys.stdin = f

mod = 10**8+7

n,m = map(int,input().split())
A,dp = [], [True]*n
for i in range(m):
    A.append(int(input()))

for a in A:
    dp[a] = False

dp[0] = 1
for now in range(n):
    for next in range
