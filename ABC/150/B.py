import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
S = input()
print(S.count('ABC'))
