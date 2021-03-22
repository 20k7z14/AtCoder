import sys
import os
f = open('test.txt','r')
sys.stdin = f

a,b,k = map(int,input().split())
divisor = []
for i in range(1,max(a,b)+1):
    if a % i == 0 and b % i == 0:
        divisor.append(i)

print(divisor[::-1][k-1])
