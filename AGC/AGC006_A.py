import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
s = set(list(input()))
t = set(list(input()))
print(len(s | t))
