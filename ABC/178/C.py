import sys
import os
f = open('test.txt','r')
sys.stdin = f

N = int(input())
MOD = 10**9 + 7

if N == 1:
    print(0)
elif N >= 2:
    a = N * (N-1)
    b = 10**(N-2) % MOD
    print(2*a*b)
