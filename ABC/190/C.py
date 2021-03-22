import sys
import os
f = open('test.txt','r')
sys.stdin = f

N,M = map(int,input().split())
condition= [list(map(int,input().split())) for i in range(M)]

K = int(input())
dish = [list(map(int,input().split())) for i in range(K)]

cond = [False] * M
for bit in range(K):
    flag = True
    d = [0] * N
    for i in range(1<<K):
        d[dish[i][bit & 1 << i]] = 1

    print(d)
