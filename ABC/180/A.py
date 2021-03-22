import sys
import os
f = open('test.txt','r')
sys.stdin = f

n,a,b = map(int,input().split())
print(n-a+b)
