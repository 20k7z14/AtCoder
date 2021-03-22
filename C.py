import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
s = [input() for i in range(n)]
print(s)
