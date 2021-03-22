import sys
import os
f = open('test.txt','r')
sys.stdin = f

n,k,m = map(int,input().split())
A = list(map(int,input().split()))

last = n*m -sum(A)
if last > k:
    print(-1)
else:
    if last < 0:
        print(0)
    else:
        print(last)
