import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
print(n*(2+(n-1))//2)
